from operator import itemgetter

class DataExtract:
    def __init__(self, fields=None):
        self.fields = list(fields.keys())
        self.types = list(fields.values())
        self.data = []

    def read(self, file):
        self.data = []
        file = open(file, "r")
        title = file.readline()

        if len(self.fields) < len(title.strip().split(',')):
            return None

        for line in file:
            data = []
            line_data = line.strip().split(',')
            field_type = 0

            for field in line_data:
                converted = self.convert(field, self.types[field_type])
                data.append(converted)
                field_type += 1

            self.data.append(data)

    def convert(self, field, field_type):
        if field_type == "str":
            return str(field)
        if field_type == "float":
            return float(field)
        if field_type == "int":
            return int(field)

    def get_field(self, name):
        data = []
        for line in self.data:
            data.append(line[self.fields.index(name)])
        return data

    def segment(self, field, by):
        data = self.get_field(field)
        by = self.get_field(by)
        groups = list(zip(data, by))
        groups = sorted(groups, key=itemgetter(1))
        dict = {}

        for value in list(set(by)):
            dict[value] = [x for (x, y) in groups if y == value]

        return dict
