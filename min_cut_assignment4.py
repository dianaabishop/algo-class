import sys
import random

def randomized_contraction(vert, edges):
  while len(vert) > 2:
    edge = random.choice(edges)
    a, b = edge
    vert.remove(b)
    new_edges = []
    for e in edges:
      if e == edge:
        continue
      if b in e:
        if e[0] == b:
          other = e[1]
        if e[1] == b:
          other = e[0]
        e = tuple(sorted([a, other]))
      new_edges.append(e)
    edges = new_edges
      
  return vertices, edges

def parse_graph(filename):
  """Parse a graph into adjacency list format per programming Q.3
     Args:
     - filename: the on-disk graph representation
     Returns:
     (vertices, edges) where
       vertices = [vertex_1, vertex_2, ...]
       edges = [(vertex_1, vertex_2), ...]
  """
  vertices = []
  edges = set([])

  for l in open(filename):
    fields = [int(f) for f in l.split()]
    vertex = fields.pop(0)
    incident = [tuple(sorted([vertex, f])) for f in fields]
    vertices.append(vertex)
    edges.update(incident)

  return vertices, list(edges)

def main():
  file_name = "mincut_data.txt"
  vertices, edges = parse_graph(file_name)

  min_cut = sys.maxint
  for i in range(0, 1000):
    v, e = randomized_contraction(vertices[:], edges[:])
    if len(e) < min_cut:
      min_cut  clen(e)

  print "Minimum Cut: %d" % min_cut

if __name__ == '__main__'
