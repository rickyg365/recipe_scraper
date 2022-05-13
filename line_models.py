import os
import json

class Heading:
    def __init__(self, input_data: str=""):
        self.text = input_data

    def __str__(self) -> str:
        txt = f"\n\n{self.text}"
        return txt

class Paragraph:
    def __init__(self, input_data: str=""):
        self.text = input_data

    def __str__(self) -> str:
        txt = f"\n{self.text}"
        return txt

class ListItem:
    def __init__(self, input_data: str=""):
        self.text = input_data

    def __str__(self) -> str:
        txt = f"- {self.text}"
        return txt
    

# def parse_data(raw_data):
#     data = []
#     for item in raw_data:
#         t, data = item['data-type'], item['data']
#         new_item = None
#         match t:
#             case "header":
#                 new_item = Heading(data)
#             case "paragraph":
#                 new_item = Paragraph(data)
#             case "list":
#                 new_item = parse_list(data)
#         data.append(new_item)

#     return data


class RecipeView:
    def __init__(self, raw_data):
        """
        Raw Data example is in test_model_data.json
        """
        self.raw_data = raw_data
        self.data = []
        
        self.cached_article = ""

        # Parse Raw Data
        self.parse_data()

    def __str__(self) -> str:
        txt = ""
        for clean in self.data:
            if (type(clean)) is list:
                for item in clean:
                    txt += f"\n{item}"
            else:
                txt += f"\n{clean}"
        self.cached_article = txt
        return txt
    
    @staticmethod
    def parse_list(input_list):
        return [ListItem(item) for item in input_list]
    
    def parse_data(self):
        """ Parses raw data by updating data """
        for item in self.raw_data:
            t, data = item['data-type'], item['data']
            new_item = None
            match t:
                case "header":
                    new_item = Heading(data)
                case "paragraph":
                    new_item = Paragraph(data)
                case "list":
                    new_item = self.parse_list(data)
                case _:
                    continue
            self.data.append(new_item)


def main():
    # Get Data, Load Json
    with open("test_model_data.json", 'r') as in_json:
        test_data = json.load(in_json)
    
    # cleaned_data = []
    # for item in test_data:
    #     t, data = item['data-type'], item['data']
    #     new_item = None
    #     match t:
    #         case "header":
    #             new_item = Heading(data)
    #         case "paragraph":
    #             new_item = Paragraph(data)
    #         case "list":
    #             new_item = parse_list(data)
    #     cleaned_data.append(new_item)

    cleaned_data = RecipeView(test_data)
    
    print(cleaned_data)

    # for clean in cleaned_data.data:
    #     if (type(clean)) is list:
    #         for item in clean:
    #             print(item)
    #     else:
    #         print(clean)
            

if __name__ == '__main__':
    main()
