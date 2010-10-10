#PyInterstate by @pygeek
import urllib2
import json

class InterstateError(Exception):
    """Base class for Interstate App Exceptions."""
    
    pass

class AuthError(InterstateError):
    """Exception raised upon authentication errors."""
    
    pass

class IdError(InterstateError):
    """Raised when an operation attempts to query's an Interstate \
        Road or Roadmap that does not exist.
        
    """
    
    pass

class InterstateApp(object):
    """Pythonic Interstate App API Wrapper
        (http://interstateapp.com)
        
        Requires:
        -Python 2.6+
        
    """
    
    __version__ = "0.2.0"
    
    def __init__(self):
        self.protocol = "http://"
        self.base_url = "interstateapp.com"
        self.api_version = "v1"
        public_key = "public-key"
        private_key = "private-key"
        
        """Installing opener authentication for inevitable, \
            subsequent requests
            
        """
        
        # create a password manager
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, self.protocol + \
            self.base_url, public_key, private_key)
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        # create "opener" (OpenerDirector instance)
        urlopener = urllib2.build_opener(handler)
        urllib2.install_opener(urlopener)

    def auth_test(self):
        """Authenticate Interstate App credentials; *public_key* : *private_key*."""
        
        listAll_url = "{0}{1}/api/{2}/roadmap/listAll" \
            .format(self.protocol, self.base_url, self.api_version)
        try:
            urllib2.urlopen(listAll_url)
        except:
            raise AuthError("Authentication Error: Please verify credentials.")
        return True
        
    def id_test(self,roadmap_id=None,road_id=None):
        """Verify whether Road or Roadmap Id exists."""
        
        roadmap_get = "{0}{1}/api/{2}/roadmap/get/id/{3}" \
            .format(self.protocol, self.base_url, self.api_version, \
            roadmap_id)
        road_get = "{0}{1}/api/{2}/road/get/id/{3}" \
            .format(self.protocol, self.base_url, self.api_version, \
            road_id)
        if roadmap_id:
            try:
                urllib2.urlopen(roadmap_get)
            except:
                raise IdError("Id Error: Roadmap Id \"{0}\" does not exist.".format(roadmap_id))
            return True
        elif road_id:
            try:
                urllib2.urlopen(road_get)
            except:
                raise IdError("Id Error: Roadmap Id \"{0}\" does not exist.".format(road_id))
            return True

class Roadmap(InterstateApp):
    """Contains methods for the Roadmap object."""

    def get(self, roadmap_id):
        """roadmap/get:
            Retrieve information regarding a specific \
            Interstate roadmap.
        Parameters:
            - id(Roadmap ID)
              The unique id of the Interstate roadmap.      
        Example Request:
            http://interstateapp.com/api/v1/roadmap/get/id/ \
              4c2d3b5f8ead0ec070010000
        Outputs: JSON
        See: http://interstateapp.com/developers/method/0/0
        
        """
        
        if self.auth_test() and self.id_test(roadmap_id=roadmap_id):
            get_url = "{0}{1}/api/{2}/roadmap/get/id/{3}" \
                .format(self.protocol, self.base_url, self.api_version, \
                roadmap_id)     
            roadmap = urllib2.urlopen(get_url)
            roadmap = roadmap.read()
            return json.loads(roadmap)
        else:
            return False
    
    def listAll(self):
        """roadmap/listAll:
            List all Interstate roadmaps associated with the \
            used API Key.
        Parameters:
            None
        Example Request:
            http://interstateapp.com/api/v1/roadmap/listAll
        Outputs: JSON
        See: http://interstateapp.com/developers/method/0/1
        
        """
        
        if self.auth_test():
            listAll_url = "{0}{1}/api/{2}/roadmap/listAll" \
                .format(self.protocol, self.base_url, self.api_version)
            roadmap = urllib2.urlopen(listAll_url)
            roadmap = roadmap.read()
            return json.loads(roadmap)
        else:
            return False
        
    def roads(self, roadmap_id):
        """roadmap/roads:
            List all roads attached to the specific Interstate roadmap.
        Parameters:
            - id(Roadmap ID)
              The unique id of the Interstate roadmap. 
        Example Request:
            http://interstateapp.com/api/v1/roadmap/roads/id/ \
              4c2d3b5f8ead0ec070010000
        Outputs: JSON
        See: http://interstateapp.com/developers/method/0/2
        
        """
        
        if self.auth_test() and self.id_test(roadmap_id=roadmap_id):
            roads_url = "{0}{1}/api/{2}/roadmap/roads/id/{3}" \
                .format(self.protocol, self.base_url, self.api_version, \
                roadmap_id)
            roadmap = urllib2.urlopen(roads_url)
            roadmap = roadmap.read()
            return json.loads(roadmap)
        else:
            return False


class Road(InterstateApp):
    """Contains methods for the Road object."""

    def get(self, road_id):
        """road/get:
            Retrieve information regarding a specific Interstate road.
        Parameters:
            - id(Road ID)
              The unique id of the Interstate road. 
        Example Request:
            http://interstateapp.com/api/v1/road/get/id/ \
              4c2d3b5f8ead0ec070010000
        Outputs: JSON
        See: http://interstateapp.com/developers/method/1/0
        
        """
        
        if self.auth_test() and self.id_test(road_id=road_id):
            get_url = "{0}{1}/api/{2}/road/get/id/{3}" \
                .format(self.protocol, self.base_url, self.api_version, \
                road_id)
            road = urllib2.urlopen(get_url)
            road = road.read()
            return json.loads(road)
        else:
            return False
        
    def updates(self, road_id):
        """road/get:
            Retrieve updates attached to a specific Interstate road.
        Parameters:
            - id(Road ID)
              The unique id of the Interstate road. 
        Example Request:
            http://interstateapp.com/api/v1/road/updates/id/
              4c2d3b5f8ead0ec070010000
        Outputs: JSON
        See: http://interstateapp.com/developers/method/1/1
        
        """
        
        if self.auth_test() and self.id_test(road_id=road_id):
            updates_url = "{0}{1}/api/{2}/road/updates/id/{3}" \
                .format(self.protocol, self.base_url, self.api_version, \
                road_id)
            road = urllib2.urlopen(updates_url)
            road = road.read()
            return json.loads(road)
        else:
            return False