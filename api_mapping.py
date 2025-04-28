import json
hb
class FieldClass:
    field_name: str
    keys: [str]
    def __init__(self, field_name: str, keys:[str]):
        self.field_name= field_name
        self.keys = keys

class ApiMapping():
    """
    Class encompassing all methods for the mapping and field map for any api defined in the api_mapping.json file.
    """
    fields = ['temp', 'temp_f', 'wind_mph', 'wind_kph', 'humidity', 'cloudcover']
    api_mapping : dict
    file_input : str
    field_mapping : [FieldClass]

    def __init__(self, file_input):
        self.file_input = file_input

    def load_mapping(self):
        """
        loads the mapping file defined in teh file_input attribute of the class
        :return:
        """
        with open(self.file_input, 'r') as file:
            data = json.load(file)
        self.api_mapping = data

    def get_formed_url(self, api: str, city: str):
        """
        Builds a full formed http/https get request for a given API
        :param api:  API name to find in the mapping file
        :param city: City name or code for API request
        :return:  A fully formed request string
        """
        formed_url = None
        api_connection_fields = self.api_mapping['apis']
        for fields in api_connection_fields:
            if fields["api_name"] == api:
                url = fields["url"]
                pre_key = fields["pre_key"]
                location_prefix = fields["location_prefix"]
                post_key = fields["post_key"]
                formed_url = f"{url}{pre_key}{location_prefix}{city}{post_key}"
        return formed_url

    def load_fields(self, api: str):
        """
        Sotes a field mapping into the class' field_mapping attribute for a given API name
        :param api:  Name of the api to retrieve the field map
        :return: None
        """
        field_mapping = []
        for apis in self.api_mapping["apis"]:
            if apis["api_name"] == api:
                for field in apis["data"]:
                    field_description = field["description"]
                    keys = []
                    for key in field["path"]:
                        keys.append(key)
                    complete_field_map = FieldClass(field_description, keys)
                    field_mapping.append(complete_field_map)
        self.field_mapping = field_mapping

    def parse_fields(self, api_json: json):
        """
        Parses the fields defined in the class fields attribute
        Adds missing fields via calculation helper methods if required
        :param api_json:  json stream of response object of API call
        :return:  dictionary of values from the response json
        """
        output = {}
        for field in self.fields:
            field_map = self.field_mapping
            for fm in field_map:
                if (fm.field_name == field):
                    key_list = fm.keys
                    try:
                        value = api_json
                        for key in key_list:
                            value = value[key]
                            print("value : " + str(value))
                            output[field] = value
                    except:
                        pass
        #cabeats for converting from metric
        if output.get("temp_f") is None:
            print(" output get temp : " + str(output.get("temp")))
            temp_f = self.c_to_f_degrees(output.get("temp"))
            output["temp_f"] = temp_f
        if output.get("wind_mph") is None:
            print(" output get temp : " + str(output.get("wind_kph")))
            wind_mph = self.kph_to_mph(output.get("wind_kph"))
            output["wind_mph"] = wind_mph
        return output

    def kph_to_mph(self, kph: float):
        """
        Convert kilometers per hour to miles per hour
        :param kph: kilometers per hour
        :return: miles per hour
        """
        return kph * (0.621371)

    def c_to_f_degrees(self, celsius: float):
        """
        Convert celsius to fahrenheit
        :param celsius: value in celsius
        :return: fahrenheit value
        """
        return ((celsius * 1.8) + 32)
