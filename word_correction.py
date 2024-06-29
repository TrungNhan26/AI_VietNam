import streamlit as st

def levenshtein_distance(token1, token2):
    # Khởi tạo ma trận khoảng cách
    distances = []
    for _ in range(len(token1) + 1):
        row = [0] * (len(token2) + 1)
        distances.append(row)


    # Khởi tạo giá trị cho hàng đầu tiên và cột đầu tiên
    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1
    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    # Tính toán khoảng cách
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                distances[t1][t2] = min(a, b, c) + 1

    # Trả về khoảng cách cuối cùng
    return distances[len(token1)][len(token2)]

def load_vocab ( file_path ) :
     with open ( file_path , 'r') as f :
        lines = f . readlines ()
        unique_words = []
        for line in lines:
            word = line.strip().lower()
            if word not in unique_words:
                unique_words.append(word)
        sorted_words = sorted(unique_words)
        return sorted_words

def main():
    st.title("Word Correction using Levenshtein Distance")
    
    # Sample vocabulary list. Replace with your actual vocabulary.
    vocabs = load_vocab ( file_path = 'C:/Users/ASUS/OneDrive - The University of Technology/Documents/Downloads/source/data/vocab.txt')

    word = st.text_input('Word:')
    
    if st.button("Compute"):
        # Compute Levenshtein distances
        leven_distances = {}
        for vocab in vocabs:
            distance = levenshtein_distance(word, vocab)
            leven_distances[vocab] = distance
        
        # Sort by distance
        sorted_distances = {}
        sorted_items = sorted(leven_distances.items(), key=lambda item: item[1])
        for item in sorted_items:
            sorted_distances[item[0]] = item[1]
        
        correct_word = list(sorted_distances.keys())[0]
        
        st.write('Correct word:', correct_word)
        
        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)
        
        col2.write('Distances:')
        col2.write(sorted_distances)

if __name__ == "__main__":
    main()
