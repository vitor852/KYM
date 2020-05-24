from os import path

"""
    # Caminho
    # Nome
    # Conteudo
"""

class File:
    def __init__(self, file):
        self.nameWExt = path.basename(file)
        self.name = path.splitext(self.nameWExt)[0]
        self.path = path.dirname(file)

        self.file = file
        
        self.content = []

        self.__get_content()

    def __get_content(self):
        try:
            with open(self.file) as file:
                for line in file:
                    self.content.append(line.strip())
        except:
            pass

    def read_file(self):
        """
            return file content
        """
        return self.content

    def __str__(self):
        return self.file