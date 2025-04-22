class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        print("Getting temperature in Celsius")
        return self._celsius

    def set_celsius(self, value):
        print(f"Setting temperature to {value} Celsius")
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value

    def del_celsius(self):
        print("Deleting temperature")
        del self._celsius

    # Create property using property(fget, fset, fdel, doc)
    celsius = property(
        fget=get_celsius,
        fset=set_celsius,
        fdel=del_celsius,
        doc="Temperature in Celsius"
    )

# Example usage
if __name__ == "__main__":
    # Create instance
    temp = Temperature(25)

    # Get temperature (calls get_celsius)
    print(f"Current temperature: {temp.celsius}")

    # Set temperature (calls set_celsius)
    temp.celsius = 30

    # Get updated temperature
    print(f"Updated temperature: {temp.celsius}")

    # Access property documentation
    print(f"Property doc: {Temperature.celsius.__doc__}")

    # Delete temperature (calls del_celsius)
    del temp.celsius

    # Try to set invalid temperature
    try:
        temp.celsius = -300
    except ValueError as e:
        print(f"Error: {e}")