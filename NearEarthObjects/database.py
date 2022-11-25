class NEODatabase:
    """A database of near-Earth objects and their close approaches.
    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """

    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.
        neos: A collection of `NearEarthObject`s.
        approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches
        
        # Create four different NEO dictionaries with different keys rispectivelly: name, designation, Hazard, Diameter
        self.neoPerName_dict = {neo.name:neo for neo in self._neos}
        self.neoPerDesignation_dict = {neo.designation:neo for neo in self._neos}
        #self.neoPerHazard_dict = {neo.diameter:neo for neo in self._neos}
        #self.neoPerDiameter_dict = {neo.hazardous:neo for neo in self._neos}
        
        # Create a dictionary having designation as keys
        self.cadPerDesignation_dict = {ca._designation:ca for ca in self._approaches}
        
       
        # Create a dictionary having designation as keys holding both cad and neo
        self.neo_cad_dict = \
            {ca:[self.neoPerDesignation_dict[ca], self.cadPerDesignation_dict[ca]] \
             for ca in self.neoPerDesignation_dict.keys()\
             if ca in self.cadPerDesignation_dict.keys()}

        self._neo_des_idx_dict = {neo.designation: idx for idx, neo in enumerate(self._neos)}

        for ca in self._approaches:
            if ca._designation in self._neo_des_idx_dict.keys():
                ca.neo = self._neos[self._neo_des_idx_dict[ca._designation]]
                self._neos[self._neo_des_idx_dict[ca._designation]].approaches.append(ca)

        
            
    def get_neo_cad_by_designation(self, designation):
        """Find and return an NEO by its primary designation
        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        try:
            return self.neo_cad_dict[designation]
        except KeyError as e:
            return e
        
        
    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation
        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        try:
            return self.neoPerDesignation_dict[designation]
        except KeyError as e:
            return e


    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.
        If no match is found, return `None` instead.
        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.
        The matching is exact - check for spelling and capitalization if no
        match is found.
        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        try:
            return self.neoPerName_dict[name]
        except KeyError as e:
            return e

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.
        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.
        If no arguments are provided, generate all known close approaches.
        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaninfully, although is often sorted by time.
        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        if filters:
            for approach in self._approaches:
                if all(map(lambda f: f(approach), filters)):
                    yield approach
        else:
            # return all the close approaches if they are no filters
            for approach in self._approaches:
                yield approach
 
 
        # create a generator producing a strem of "CloseApproach" objects
        #(ca for ca in self._approaches if all(map(lambda x: x(ca), filters)))