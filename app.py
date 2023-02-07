import streamlit as st
st.set_page_config(layout="wide")

import requests
import json


hide_footer_style = """
<style>
header {
    display: none !important;
}
footer {
    display: none !important;
}
section > div.block-container {
    padding-top: 0px !important;
    padding-bottom: 0px !important;
}
h1,
h2,
h3,
h4,
h5,
h6,
p,
span,
div {
  font-family: "Roboto", sans-serif !important;
  font-weight: 500;
}
[data-baseweb="slider"] {
    padding-left: 10px !important;
}
#MainMenu {
    visibility: hidden;
}
footer {
    visibility: hidden;
}
.modebar{
      display: none !important;
}
</style>
"""
st.write(hide_footer_style, unsafe_allow_html=True)

query_params = st.experimental_get_query_params()
mode = query_params.get("mode", ["uk"])[0]

if mode == "uk":
    with st.expander("Compute current-law taxes and benefits", expanded=True):
        default_situation = {
            "household": {
                "people": {
                    "parent": {
                        "age": {2023: 35},
                        "employment_income": {2023: 30_000},
                    },
                    "child": {
                        "age": {2023: 10},
                    },
                },
                "households": {
                    "household": {
                        "members": ["parent", "child"],
                        "household_net_income": {2023: None},
                        "household_benefits": {2023: None},
                        "household_tax": {2023: None},
                    },
                },
            },
        }
        data_input, api_output, code_snippet = st.tabs(
            ["JSON input", "API output", "Python snippet"]
        )
        with data_input:
            st.caption("Describe people and households")
            situation = data_input.text_area(
                "Situation",
                value=json.dumps(default_situation, indent=4),
                height=300,
            )
            result = requests.post(
                "https://api.policyengine.org/uk/calculate",
                json=json.loads(situation),
            ).json()

        with code_snippet:
            code_snippet = f"""import requests
import json

situation = {situation}
result = requests.post("https://api.policyengine.org/uk/calculate", json=situation).json()
print(json.dumps(result, indent=4))"""
            st.caption("Python code snippet")
            st.code(code_snippet)

        with api_output:
            st.caption("PolicyEngine's API computes their taxes and benefits")
            st.json(result)

    with st.expander("Compute impacts of reforms"):
        default_situation = {
            "household": {
                "people": {
                    "parent": {
                        "age": {2023: 35},
                        "employment_income": {2023: 30_000},
                    },
                    "child": {
                        "age": {2023: 10},
                    },
                },
                "households": {
                    "household": {
                        "members": ["parent", "child"],
                        "household_net_income": {2023: None},
                        "household_benefits": {2023: None},
                        "household_tax": {2023: None},
                    },
                },
            },
            "policy": {
                "gov.hmrc.income_tax.rates.uk[0].rate": {
                    "2023-01-01.2024-01-01": 0.25,
                }
            },
        }
        data_input, api_output, code_snippet = st.tabs(
            ["JSON input", "API output", "Python snippet"]
        )
        with data_input:
            st.caption("Describe people, households and reforms")
            situation = data_input.text_area(
                "Situation and reform",
                value=json.dumps(default_situation, indent=4),
                height=300,
            )
            result = requests.post(
                "https://api.policyengine.org/uk/calculate",
                json=json.loads(situation),
            ).json()

        with code_snippet:
            code_snippet = f"""import requests
import json

situation = {situation}
result = requests.post("https://api.policyengine.org/uk/calculate", json=situation).json()
print(json.dumps(result, indent=4))"""
            st.caption("Python code snippet")
            st.code(code_snippet)

        with api_output:
            st.caption("PolicyEngine's API computes their taxes and benefits")
            st.json(result)


if mode == "us":
    with st.expander("Compute current-law taxes and benefits", expanded=True):
        default_situation = {
            "people": {
                "parent": {
                    "age": {2023: 35},
                    "employment_income": {2023: 30_000},
                },
                "child": {
                    "age": {2023: 10},
                },
            },
            "households": {
                "household": {
                    "members": ["parent", "child"],
                    "household_net_income": {2023: None},
                    "household_benefits": {2023: None},
                    "household_tax": {2023: None},
                },
            },
        }
        data_input, api_output, code_snippet = st.tabs(
            ["JSON input", "API output", "Code snippet"]
        )
        with data_input:
            st.caption("Describe people and households")
            situation = data_input.text_area(
                "Situation",
                value=json.dumps(default_situation, indent=4),
                height=300,
            )
            result = requests.post(
                "https://api.policyengine.org/us/calculate",
                json={
                    "household": json.loads(situation),
                },
            ).json()

        with code_snippet:
            code_snippet = f"""import requests
import json

situation = {situation}
result = requests.post("https://api.policyengine.org/us/calculate", json=situation).json()
print(json.dumps(result, indent=4))"""
            st.caption("Python code snippet")
            st.code(code_snippet)

        with api_output:
            st.caption("PolicyEngine's API computes their taxes and benefits")
            st.json(result)

    with st.expander("Compute impacts of reforms"):
        default_situation = {
            "household": {
                "people": {
                    "parent": {
                        "age": {2023: 35},
                        "employment_income": {2023: 30_000},
                    },
                    "child": {
                        "age": {2023: 10},
                    },
                },
                "households": {
                    "household": {
                        "members": ["parent", "child"],
                        "household_net_income": {2023: None},
                        "household_benefits": {2023: None},
                        "household_tax": {2023: None},
                    },
                },
            },
            "policy": {
                "gov.usda.snap.income.deductions.earned_income": {
                    "2023-01-01.2024-01-01": 0.25,
                }
            },
        }
        data_input, api_output, code_snippet = st.tabs(
            ["JSON input", "API output", "Code snippet"]
        )
        with data_input:
            st.caption("Describe people, households and reforms")
            situation = data_input.text_area(
                "Situation and reform",
                value=json.dumps(default_situation, indent=4),
                height=300,
            )
            result = requests.post(
                "https://api.policyengine.org/us/calculate",
                json=json.loads(situation),
            ).json()

        with code_snippet:
            code_snippet = f"""import requests
import json

situation = {situation}
result = requests.post("https://api.policyengine.org/us/calculate", json=situation).json()
print(json.dumps(result, indent=4))"""
            st.caption("Python code snippet")
            st.code(code_snippet)

        with api_output:
            st.caption("PolicyEngine's API computes their taxes and benefits")
            st.json(result)
