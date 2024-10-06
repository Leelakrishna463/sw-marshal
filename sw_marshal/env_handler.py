import environ

env = environ.Env()

ENV_VAR = {}

ENV_VAR['DB_PASS_VAULT_NAME'] = env.str('DB_PASS_VAULT_NAME')
ENV_VAR['DB_PG_HOST'] = env.str('DB_PG_HOST')
ENV_VAR['DB_PG_PASSWORD'] = env.str('DB_PG_PASSWORD')
ENV_VAR['DB_PG_USERNAME'] = env.str('DB_PG_USERNAME')
ENV_VAR['DB_SW_MARSHAL_NAME'] = env.str('DB_SW_MARSHAL_NAME')
ENV_VAR['DEBUG'] = env.str('DEBUG')
ENV_VAR['SECRET_KEY'] = env.str('SECRET_KEY')
ENV_VAR['PW_APP_LOGO_PATH'] = env.str('PW_APP_LOGO_PATH')
