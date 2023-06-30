from InstructorEmbedding import INSTRUCTOR
# model = INSTRUCTOR('hkunlp/instructor-large')
model = INSTRUCTOR('/home/ubuntu/yzq/models/instructor-large')
sentence = "3D ActionSLAM: wearable person tracking in multi-floor environments"
instruction = "Represent the Science title:"
embeddings = model.encode([[instruction,sentence]])
print(embeddings)