#Interstate App Library
import urllib2
import os
import json

class InterstateApp(object):
    """
        Pythonic InterstateApp API Wrapper
        (http://interstateapp.com)
        
        Requires:
        -Python 2.6+
    """
    def __init__(self):
        self.protocol = "http://"
        self.base_url = "interstateapp.com"
        self.api_version = "v1"
        public_key = "public_key"
        private_key = "private_key"
        
        """
            Installing opener authentication for inevitable,\
            subsequent requests
        """
        # create a password manager
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, self.protocol+self.base_url,\
            public_key, private_key)
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        # create "opener" (OpenerDirector instance)
        urlopener = urllib2.build_opener(handler)
        urllib2.install_opener(urlopener)

class Roadmap(InterstateApp):

    def get(self,roadmap_id):
        """
        roadmap/get:
            Retrieve information regarding a specific Interstate roadmap.
        Parameters:
            - id(Roadmap ID)
              The unique id of the Interstate roadmap.      
        Example Request:
            http://interstateapp.com/api/v1/roadmap/get/id/\
              4c2d3b5f8ead0ec070010000
        Outputs: JSON
        See: http://interstateapp.com/developers/method/0/0  
        """
        get_url = "{0}{1}/api/{2}/roadmap/get/id/{3}"\
            .format(self.protocol,self.base_url,self.api_version\
            ,roadmap_id)
        roadmap = urllib2.urlopen(get_url)
        roadmap = roadmap.read()
        return json.loads(roadmap)
    
    def listAll(self):
        """
        roadmap/listAll:
            List all Interstate roadmaps associated with the used API Key.
        Parameters:
            None
        Example Request:
            http://interstateapp.com/api/v1/roadmap/listAll
        Outputs: JSON
        See: http://interstateapp.com/developers/method/0/1
        """
        listAll_url = "{0}{1}/api/{2}/roadmap/listAll"\
            .format(self.protocol,self.base_url,self.api_version)
        roadmap = urllib2.urlopen(listAll_url)
        roadmap = roadmap.read()
        return json.loads(roadmap)
        
    def roads(self,roadmap_id):
        """
        roadmap/roads:
            List all roads attached to the specific Interstate roadmap.
        Parameters:
            - id(Roadmap ID)
              The unique id of the Interstate roadmap. 
        Example Request:
            http://interstateapp.com/api/v1/roadmap/roads/id/\
              4c2d3b5f8ead0ec070010000
        Outputs: JSON
        See: http://interstateapp.com/developers/method/0/2
        """
        roads_url = "{0}{1}/api/{2}/roadmap/roads/id/{3}"\
            .format(self.protocol,self.base_url,self.api_version\
            ,roadmap_id)
        roadmap = urllib2.urlopen(roads_url)
        roadmap = roadmap.read()
        return json.loads(roadmap)


class Road(InterstateApp):

    def get(self,road_id):
        """
        road/get:
            Retrieve information regarding a specific Interstate road.
        Parameters:
            - id(Road ID)
              The unique id of the Interstate road. 
        Example Request:
            http://interstateapp.com/api/v1/road/get/id/\
              4c2d3b5f8ead0ec070010000
        Outputs: JSON
        See: http://interstateapp.com/developers/method/1/0
        """
        get_url = "{0}{1}/api/{2}/road/get/id/{3}"\
            .format(self.protocol,self.base_url,self.api_version\
            ,road_id)
        road = urllib2.urlopen(get_url)
        road = road.read()
        return json.loads(road)
        
    def updates(self,road_id):
        """
        road/get:
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
        updates_url = "{0}{1}/api/{2}/road/updates/id/{3}"\
            .format(self.protocol,self.base_url,self.api_version\
            ,road_id)
        road = urllib2.urlopen(updates_url)
        road = road.read()
        return json.loads(road)