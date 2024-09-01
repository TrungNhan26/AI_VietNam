### Question 1
import numpy as np
import pandas as pd


def compute_mean (x) :
# your code here *********************
    s = sum(x)
    mean = s/len(x)
    return mean

X = [2 , 0 , 2 , 2 , 7, 4 , -2 , 5 , -1 , -1]
print (" Mean: ", compute_mean(X))

### Question 2
def compute_median(X):
    size = len(X)
    X = np.sort(X)
    print(X)
    if size % 2 == 0:
        # Trung vị là giá trị trung bình của hai phần tử giữa
        return (X[size//2 - 1] + X[size//2]) / 2
    else:
        # Trung vị là phần tử giữa
        return X[size//2]

X = [1 , 5 , 4 , 4 , 9, 13]
print (" Median : ", compute_median ( X ) )

### Question 3
def compute_std ( X ) :
    mean = compute_mean ( X )
    variance = 0
    for i in X:
        variance += (i - mean) ** 2
    variance = variance / len(X)
    # your code here *******************
    return np.sqrt( variance )

X = [ 171 , 176 , 155 , 167 , 169 , 182]
print ( round(compute_std ( X ),2) )

###Question 4
def compute_correlation_cofficient(X, Y):
    N = len(X)  # Number of elements
    sum_XY = np.sum(X * Y)  # Sum of the products of X and Y
    sum_X = np.sum(X)  # Sum of X
    sum_Y = np.sum(Y)  # Sum of Y
    sum_X2 = np.sum(X ** 2)  # Sum of squares of X
    sum_Y2 = np.sum(Y ** 2)  # Sum of squares of Y

    # Calculate the numerator of the correlation coefficient formula
    numerator = N * sum_XY - sum_X * sum_Y

    # Calculate the denominator of the correlation coefficient formula
    denominator = np.sqrt((N * sum_X2 - sum_X ** 2) * (N * sum_Y2 - sum_Y ** 2))

    # Return the correlation coefficient rounded to 2 decimal places
    return np.round(numerator / denominator, 2)

# Input data
X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
# Compute and print the correlation coefficient
print("Correlation:", compute_correlation_cofficient(X, Y))


import gdown
# # URL Google Drive có chứa file cần tải
# url = "https://drive.google.com/uc?id=1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq"
output = "advertising.csv"  # Tên file sau khi tải về
data = pd.read_csv(output)
# Example usage :
x = data ['TV']
y = data ['Radio']
corr_xy = compute_correlation_cofficient(x , y )
print ( f" Correlation between TV and Sales : { round ( corr_xy , 2)}")

features = ['TV', 'Radio', 'Newspaper']  # Đóng dấu nháy đơn đúng cách
for feature_1 in features:
    for feature_2 in features:
        correlation_value = compute_correlation_cofficient(data[feature_1], data[feature_2])  # Thụt lề đúng
        print(f"Correlation between {feature_1} and {feature_2}: {correlation_value:.2f}")  # In kết quả với 2 chữ số thập phân


# Đọc dữ liệu từ file CSV
data = pd.read_csv("advertising.csv")
# Lấy dữ liệu cho các biến cần tính tương quan
x = data['Radio']
y = data['Newspaper']

# Tính ma trận tương quan giữa hai biến
correlation_matrix = np.corrcoef(x, y)
# In ra kết quả
print(correlation_matrix)


data = pd.read_csv("advertising.csv")
print(data.corr())

# Question 09
import matplotlib . pyplot as plt
import seaborn as sns

data = pd.read_csv ("advertising.csv")
plt . figure ( figsize =(10 ,8) )
data_corr = data.corr()
sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)
plt.show ()


import requests
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# URL của tệp CSV
url = "https://drive.google.com/uc?id=1jh2p2DlaWsDo_vEWIcTrNh3mUuXd-cw6"
output2 = "vi_text_retrieval.csv"  # Tên file sau khi tải về

# Tải tệp từ URL và lưu vào ổ đĩa
response = requests.get(url)
with open(output2, "wb") as file:
    file.write(response.content)

# Đọc tệp CSV đã tải xuống
vi_data_df = pd.read_csv(output2)

# Trích xuất và tiền xử lý văn bản
context = vi_data_df['text']
context = [doc.lower() for doc in context]

# Khởi tạo vectorizer và chuyển đổi văn bản thành vector TF-IDF
tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)

# Trích xuất giá trị TF-IDF của document thứ 8 (chỉ số 7)
value = context_embedded.toarray()[7][0]

print("Giá trị TF-IDF tại vị trí [7][0]:", value)

from sklearn.metrics.pairwise import cosine_similarity


def tfidf_search(question, tfidf_vectorizer, top_d=5):
    # Lowercasing before encoding
    question = question.lower()

    # Chuyển câu hỏi thành vector TF-IDF
    query_embedded = tfidf_vectorizer.transform([question])

    # Tính toán độ tương đồng cosine giữa câu hỏi và các văn bản
    cosine_scores = cosine_similarity(query_embedded, context_embedded).flatten()

    # Lấy top k điểm số cosine và chỉ số của chúng
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc_score)

    return results


# Sử dụng hàm tfidf_search
question = vi_data_df.iloc[0]['question']
results = tfidf_search(question, tfidf_vectorizer, top_d=5)
print("Cosine score của kết quả đầu tiên:", results[0]['cosine_score'])

from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import correlation


def corr_search(question, tfidf_vectorizer, top_d=5):
    # Lowercasing before encoding
    question = question.lower()

    # Chuyển câu hỏi thành vector TF-IDF
    query_embedded = tfidf_vectorizer.transform([question])

    # Tính toán ma trận tương quan giữa câu hỏi và các văn bản
    # Đầu tiên, chuyển đổi ma trận TF-IDF thành dạng ma trận numpy để tính toán tương quan
    context_embedded_np = context_embedded.toarray()
    query_embedded_np = query_embedded.toarray().flatten()

    # Tính toán độ tương quan (correlation) giữa vector câu hỏi và tất cả các vector văn bản
    corr_scores = np.array([correlation(query_embedded_np, doc) for doc in context_embedded_np])

    # Chỉ lấy các giá trị tương quan khác ngoài giá trị đầu tiên (có thể do lỗi tính toán)
    corr_scores = corr_scores[1:]

    # Lấy top k điểm số tương quan và chỉ số của chúng
    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx + 1,  # Cộng 1 để điều chỉnh chỉ số cho phù hợp
            'corr_score': corr_scores[idx]
        }
        results.append(doc)

    return results


# Sử dụng hàm corr_search
question = vi_data_df.iloc[0]['question']
results = corr_search(question, tfidf_vectorizer, top_d=5)
print("Correlation score của kết quả thứ hai:", results[1]['corr_score'])
