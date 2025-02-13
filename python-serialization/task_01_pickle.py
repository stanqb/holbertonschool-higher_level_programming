import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        :param name: Name of the person (string)
        :param age: Age of the person (integer)
        :param is_student: Student status (boolean)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in the required format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        :param filename: The file to save the serialized object
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        :param filename: The file containing the serialized object
        :return: An instance of CustomObject or None if an error occurs
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
