

def build_card_name(item: dict) -> str:
    return f"{item['story_id']} – {item['system_component']}"


def build_card_description(item: dict) -> str:
    return f"""
### 📌 Story ID
{item['story_id']}

### 🧱 Component
{item['system_component']}

### ⏱️ Estimation
- Base: {item['base_estimate_hours']} hrs
- TCF: {item['tcf']}
- AEF: {item['aef']}
- **Final:** {item['final_estimate_hours']} hrs

### ⚠️ Risk
{item['risk_level']}

### 🧠 Justification
{item['justification']}

---
✅ Definition of Done
- Code complete
- Tests pass
- Reviewed
""".strip()
