from transformers import pipeline

# 加载文本摘要模型 
summarizer = pipeline("summarization")

# 长文本
long_text = """
这是一段非常长的文本，包含了大量的内容。在压缩文本时，我们希望将这段长文本缩减为短文本摘要，保留其中的关键信息，同时减少冗余和重复内容。这样做可以提供一个简洁的概述，使人们更容易理解和获取文本的主要要点。使用transformers库中的pipeline可以轻松实现这一目标。
"""

# 对长文本进行摘要
short_summary = summarizer(long_text, max_length=50, min_length=10, do_sample=False)[0]['summary_text']

print("原文本：\n", long_text)
print("\n摘要：\n", short_summary)

long_text="I believe Logrus' biggest contribution is to have played a part in today's widespread use of structured logging in Golang. There doesn't seem to be a reason to do a major, breaking iteration into Logrus V2, since the fantastic Go community has built those independently. Many fantastic alternatives have sprung up. Logrus would look like those, had it been re-designed with what we know about structured logging in Go today. Check out, for example, Zerolog, Zap, and Apex."
short_summary = summarizer(long_text, max_length=50, min_length=10, do_sample=False)[0]['summary_text']

print("\n摘要：\n", short_summary)