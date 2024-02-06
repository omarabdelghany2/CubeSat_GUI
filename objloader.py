class OBJ:
    def __init__(self, filename, swapyz=False):
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        self.load(filename, swapyz)

    def load(self, filename, swapyz):
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                values = line.split()
                if not values:
                    continue
                if values[0] == 'v':
                    vertex = list(map(float, values[1:4]))
                    if swapyz:
                        vertex = [vertex[0], vertex[2], -vertex[1]]
                    self.vertices.append(vertex)
                elif values[0] == 'vn':
                    normal = list(map(float, values[1:4]))
                    if swapyz:
                        normal = [normal[0], normal[2], -normal[1]]
                    self.normals.append(normal)
                elif values[0] == 'vt':
                    texcoord = list(map(float, values[1:3]))
                    self.texcoords.append(texcoord)
                elif values[0] == 'f':
                    face = []
                    texcoords = []
                    norms = []
                    for v in values[1:]:
                        w = v.split('/')
                        face.append(int(w[0]))
                        if len(w) >= 2 and len(w[1]) > 0:
                            texcoords.append(int(w[1]))
                        else:
                            texcoords.append(0)
                        if len(w) >= 3 and len(w[2]) > 0:
                            norms.append(int(w[2]))
                        else:
                            norms.append(0)
                    self.faces.append((face, norms, texcoords))
