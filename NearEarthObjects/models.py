from helpers import cd_to_datetime, datetime_to_str

class NearEarthObject:
    
    def __init__(self, designation, name = None, diameter = "", hazardous = "" , **info):
        """`NearEarthObject` object
        designation (str), param name (str), diameter (float), hazardous ('str'), param approaches (list)
        """
        self.designation = str(designation)
        
        if name.strip() == "":
            self.name = None
        else:
            self.name = str(name.strip())
        
        try:
            self.diameter = float(diameter)
        except ValueError:
            self.diameter = float("nan")
            
        if hazardous.lower() == "y":
            self.hazardous = True
        else:
            self.hazardous = False

        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO - Near Earth Object, 
                which is the designation and eventually a name provided by NASA"""
            
        if self.name == None:
            return f"{self.designation}"
        else:
            return f"{self.designation} ({self.name})"

    def __str__(self):
        """Return `str(self)`."""
        
        if self.name == None:
            name_string = f"The {self.designation} Near Earth Object for which we have not a name yet,"
        else:
            name_string = f" The {self.name} Near Earth Object,"
        
        
        if self.hazardous is False:
            isHazardous = " not"
        else:
            isHazardous = ""

        if self.diameter == 0.0:
            diameter_string = "has a not known diameter"
        else:
            diameter_string = f"has a diameter of {self.diameter:.3f} km"
            
        return f"{name_string} {diameter_string} and it is calssified as {isHazardous} hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")




class CloseApproach:

    def __init__(self, designation, time, distance, velocity, **info):
        """Create a new `CloseApproach` 
        designation (str), 
        time (es 2014-May-14 13:20), 
        distance (float), 
        velocity (float), 
        neo (Object)
        """
        self._designation = str(designation)
        self.time =  cd_to_datetime(time) # I use cd_to_datetime function for this attribute.
        self.distance = float(distance)
        self.velocity = float(velocity)
        self.neo = None # Create an attribute for the referenced NEO, originally None.

    @property
    def time_str(self):
         return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        return f"On {self.time_str}, {self.neo.fullname} approaches Earth at a distance of {self.distance:.3f} au and a velocity of {self.velocity:.3f} km/s."
    

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")