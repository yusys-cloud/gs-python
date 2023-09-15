from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 文本数据
text1 = "This is the first document."
text2 = "This document is the second document."

# 创建TF-IDF向量化器
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([text1, text2])

# 计算余弦相似度
similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
print(similarity[0][0])
