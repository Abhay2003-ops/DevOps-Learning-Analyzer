
import user_inputs
import constants  

def run():
    print(f"\n🔹 Welcome to {constants.APP_NAME} 🔹\n")


    user_data = user_inputs.get_basic_user_info()

    print("\n✅ User Information Collected:")
    print(f"Name: {user_data['name']}")
    print(f"Education: {user_data['education']}")
    print(f"Expertise Level: {user_data['expertise']}")

if __name__ == "__main__":
    run()


