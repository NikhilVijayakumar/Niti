import os
import re
from typing import Dict, Any

from amsha.crew_forge import AmshaCrewFileApplication
from amsha.llm_factory.domain.model.llm_type import LLMType

from src.nikhil.niti.config.settings import Settings
from src.nikhil.niti.domain.context_preperation.model.product_backlog import ProductBacklog


class ContextLeadershipApplication(AmshaCrewFileApplication):

    def __init__(self, config_paths: Dict[str, str],llm_type:LLMType):

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

            # Regex to capture content inside ```json ... ``` or just ``` ... ```
            # flags=re.DOTALL allows . to match newlines
            pattern = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL)
            match = pattern.search(content)

            new_content = content
            if match:
                print(f"  -> Found markdown code block in {os.path.basename(file_path)}. Stripping it.")
                new_content = match.group(1).strip()
            else:
                # Fallback: just strip whitespace
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
                pipeline_input["brd_content"] = next_input["brd_content"]
                print(f"{class_name} - pipeline_input:{pipeline_input}")
                result = None
                max_retries = 10
                retry_delay = 60
                
                for attempt in range(max_retries):
                    try:
                        result = self.orchestrator.run_crew(
                            crew_name=crew_name,
                            inputs=pipeline_input,
                            output_json=ProductBacklog
                        )
                        
                        # Validate output immediately inside the loop
                        output_file = self.orchestrator.get_last_output_file()
                        if output_file:
                            print(f"{class_name}:{output_file}")
                            
                            # 1. Sanitize (remove markdown)
                            self._sanitize_json_content(output_file)
                            
                            # 2. Clean/Validate JSON structure
                            # clean_json returns True if valid/fixed, False otherwise.
                            is_valid = self.clean_json(output_file)
                            if not is_valid:
                                raise ValueError(f"JSON validation failed for {output_file}")
                        
                        # If we reached here, result is good (or at least valid JSON)
                        break 
                        
                    except Exception as e:
                        # Handle Rate Limits
                        if "RateLimitError" in str(e) and attempt < max_retries - 1:
                            print(f"Rate limit hit (Attempt {attempt + 1}/{max_retries}). Waiting {retry_delay}s for quota reset...")
                            import time
                            time.sleep(retry_delay)
                            continue
                            
                        # Handle Validation Errors (Retry if possible)
                        if "JSON validation failed" in str(e) and attempt < max_retries - 1:
                            print(f"Validation failed (Attempt {attempt + 1}/{max_retries}): {e}. Retrying...")
                            continue

                        # Final attempt failed or non-retryable error
                        if attempt >= max_retries - 1:
                            print(f"Final attempt failed: {e}")
                            raise e
                        else:
                            # Other unexpected errors, maybe retry? 
                            # For safety, let's retry on generic errors too if you prefer, 
                            # or re-raise. The original code re-raised generic errors immediately
                            # except RateLimit. Let's stick closer to safely retrying only known issues
                            # or strictly following the original logic for other exceptions.
                            # Original logic: raise e unless RateLimit. 
                            # I will raise e to be safe, unless it's strictly the new Validation error I added.
                            print(f"Non-retryable error encountered: {e}")
                            raise e


                results_for_list.append(result)
            pipeline_results[crew_name] = results_for_list
        return pipeline_results


if __name__ == "__main__":
    # Configuration is now neatly defined in one place.
    configs = {
        "llm": Settings.LLM_CONFIG,
        "app": Settings.APP_CONFIG,
        "job": "/home/user/Arsha/Niti/src/nikhil/niti/domain/context_preperation/config/context_leadership_config.yaml"
    }

    # The main script is now incredibly simple and clean.
    app = ContextLeadershipApplication(config_paths=configs,llm_type=LLMType.CREATIVE)
    app.run()


