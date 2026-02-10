
import venv
import os

# Path where you want to create the environment
env_path = os.path.join(os.getcwd(), "graphenv2")

# Create the virtual environment
venv.create(env_path, with_pip=True)

print(f"Virtual environment created at: {env_path}")
print("Activate it using:")
print(f"  source {env_path}/bin/activate   # On Linux/Mac")
print(f"  {env_path}\\Scripts\\activate    # On Windows")
