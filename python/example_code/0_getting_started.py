import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion


"""
OPENAI_ORG_ID=""
AZURE_OPENAI_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_AISEARCH_API_KEY=""
AZURE_AISEARCH_URL=""
"""

# setup using openAI key
kernel = sk.Kernel()
api_key, org_id = sk.openai_settings_from_dot_env()

kernel.add_chat_service("chat-gpt", OpenAIChatCompletion(ai_model_id="gpt-3.5-turbo", api_key=api_key, org_id=org_id))

# run a function
skill = kernel.import_semantic_skill_from_directory("../../samples/skills", "FunSkill")
joke_function = skill["Joke"]

print(joke_function("time travel to dinosaur age"))
