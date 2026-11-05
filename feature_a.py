"""
Feature A
Doctor Search Module
"""

doctors = [
    {
        "id": 101,
        "name": "Dr. Sharma",
        "specialization": "Cardiologist"
    },
    {
        "id": 102,
        "name": "Dr. Verma",
        "specialization": "Dermatologist"
    },
    {
        "id": 103,
        "name": "Dr. Kumar",
        "specialization": "Neurologist"
    }
]


def view_doctors():
    print("\nAvailable Doctors\n")

    for doctor in doctors:
        print(
            f"ID: {doctor['id']} | "
            f"Name: {doctor['name']} | "
            f"Specialization: {doctor['specialization']}"
        )


if __name__ == "__main__":
    view_doctors()