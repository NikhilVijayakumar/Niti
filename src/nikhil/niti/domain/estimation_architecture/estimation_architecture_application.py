import os
import re
from typing import Dict, Any

from amsha.crew_forge import AmshaCrewFileApplication
from amsha.llm_factory.domain.model.llm_type import LLMType

from src.nikhil.niti.config.settings import Settings
from src.nikhil.niti.domain.estimation_architecture.model.consensus_report import ConsensusReport


class EstimationArchitectureApplication(AmshaCrewFileApplication):

    def __init__(self, config_paths: Dict[str, str], llm_type: LLMType):
        super().__init__(config_paths, llm_type)

    def _sanitize_json_content(self, file_path: str):
        """
        Removes markdown code blocks (e.g. ```json ... ```) from the file content
        to ensure it contains only raw JSON.
        """
        if not os.path.exists(file_path):
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            pattern = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL)
            match = pattern.search(content)

            new_content = content
            if match:
                print(f"  -> Found markdown code block in {os.path.basename(file_path)}. Stripping it.")
                new_content = match.group(1).strip()
            else:
                new_content = content.strip()

            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

        except Exception as e:
            print(f"Warning: Failed to sanitize JSON content in {file_path}: {e}")

    def run(self) -> Any:
        class_name = self.__class__.__name__
        print(f"{class_name} - Starting configured pipeline workflow...")

        pipeline_steps = self.job_config.get("pipeline", [])
        if not pipeline_steps:
            print("No pipeline defined in job_config.yaml. Nothing to run.")
            return

        pipeline_results = {}
        results_for_list = []
        pipeline_input = {}

        for crew_name in pipeline_steps:
            if not pipeline_results:
                next_input = self._prepare_multiple_inputs_for(crew_name)

                # CREW-02 inputs
                pipeline_input["product_backlog"] = next_input["product_backlog"]
                pipeline_input["team_profile"] = next_input["team_profile"]

                print(f"{class_name} - pipeline_input keys: {list(pipeline_input.keys())}")

                result = None
                max_retries = 10
                retry_delay = 60

                for attempt in range(max_retries):
                    try:
                        result = self.orchestrator.run_crew(
                            crew_name=crew_name,
                            inputs=pipeline_input,
                            output_json=ConsensusReport
                        )

                        output_file = self.orchestrator.get_last_output_file()
                        if output_file:
                            print(f"{class_name}:{output_file}")

                            # 1. Sanitize markdown wrappers
                            self._sanitize_json_content(output_file)

                            # 2. Validate / clean JSON
                            is_valid = self.clean_json(output_file)
                            if not is_valid:
                                raise ValueError(f"JSON validation failed for {output_file}")

                        # Success
                        break

                    except Exception as e:
                        # Rate limit handling
                        if "RateLimitError" in str(e) and attempt < max_retries - 1:
                            print(
                                f"Rate limit hit (Attempt {attempt + 1}/{max_retries}). "
                                f"Waiting {retry_delay}s for quota reset..."
                            )
                            import time
                            time.sleep(retry_delay)
                            continue

                        # Validation retry
                        if "JSON validation failed" in str(e) and attempt < max_retries - 1:
                            print(
                                f"Validation failed (Attempt {attempt + 1}/{max_retries}): {e}. Retrying..."
                            )
                            continue

                        # Final failure
                        if attempt >= max_retries - 1:
                            print(f"Final attempt failed: {e}")
                            raise e
                        else:
                            print(f"Non-retryable error encountered: {e}")
                            raise e

                results_for_list.append(result)

            pipeline_results[crew_name] = results_for_list

        return pipeline_results


if __name__ == "__main__":

    configs = {
        "llm": Settings.LLM_CONFIG,
        "app": Settings.APP_CONFIG,
        "job": "/home/user/Arsha/Niti/src/nikhil/niti/domain/estimation_architecture/config/estimation_architecture_config.yaml"
    }

    app = EstimationArchitectureApplication(
        config_paths=configs,
        llm_type=LLMType.EVALUATION
    )
    app.run()
