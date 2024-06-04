import toml

output_file = ".streamlit/secrets.toml"

with open("test-a8f18-firebase-adminsdk-s2dh5-e23ffba0f8.json") as json_file:
    json_text = json_file.read()

config = {"textkey": json_text}
toml_config = toml.dumps(config)

with open(output_file, "w") as target:
    target.write(toml_config)
