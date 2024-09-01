import numpy as np

def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'no'],
        ['Sunny', 'Hot', 'High', 'Strong', 'no'],
        ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'no'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'yes']
    ]
    return np.array(data)

def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))

    total_samples = len(train_data)
    print(total_samples)
    count_no = np.sum(train_data[:, -1] == 'no')
    count_yes = np.sum(train_data[:, -1] == 'yes')

    prior_probability[0] = count_no / total_samples
    prior_probability[1] = count_yes / total_samples

    return prior_probability

def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []
    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        x_conditional_probability = []

        for x in x_unique:
            count_x_given_no = np.sum((train_data[:, i] == x) & (train_data[:, -1] == 'no'))
            count_x_given_yes = np.sum((train_data[:, i] == x) & (train_data[:, -1] == 'yes'))

            total_no = np.sum(train_data[:, -1] == 'no')
            total_yes = np.sum(train_data[:, -1] == 'yes')

            prob_x_given_no = count_x_given_no / total_no if total_no > 0 else 0
            prob_x_given_yes = count_x_given_yes / total_yes if total_yes > 0 else 0

            x_conditional_probability.append((prob_x_given_no, prob_x_given_yes))

        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name

def get_index_from_value(feature_name, list_features):
    indices = np.where(list_features == feature_name.strip())[0]
    if len(indices) > 0:
        return indices[0]
    else:
        raise ValueError(f"'{feature_name.strip()}' không có trong danh sách các thuộc tính.")

def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probability(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(train_data)

    return prior_probability, conditional_probability, list_x_name

def get_index_from_value(value, list_x_name):
    return list_x_name.index(value)

def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])  # Outlook
    x2 = get_index_from_value(X[1], list_x_name[1])  # Temperature
    x3 = get_index_from_value(X[2], list_x_name[2])  # Humidity
    x4 = get_index_from_value(X[3], list_x_name[3])  # Wind

    p0 = prior_probability[0]  # P(PlayTennis=0)
    p1 = prior_probability[1]  # P(PlayTennis=1)

    # Tính toán xác suất cho mỗi lớp dựa trên các thuộc tính
    p0 *= conditional_probability[0][x1]  # P(Outlook | PlayTennis=0)
    p0 *= conditional_probability[1][x2]  # P(Temperature | PlayTennis=0)
    p0 *= conditional_probability[2][x3]  # P(Humidity | PlayTennis=0)
    p0 *= conditional_probability[3][x4]  # P(Wind | PlayTennis=0)

    p1 *= conditional_probability[4][x1]  # P(Outlook | PlayTennis=1)
    p1 *= conditional_probability[5][x2]  # P(Temperature | PlayTennis=1)
    p1 *= conditional_probability[6][x3]  # P(Humidity | PlayTennis=1)
    p1 *= conditional_probability[7][x4]  # P(Wind | PlayTennis=1)

    if p0 > p1:
        y_pred = 0  # Không chơi tennis
    else:
        y_pred = 1  # Chơi tennis

    return y_pred

#4.1
train_data = create_train_data()
print(train_data)

#4.2
prior_probablity = compute_prior_probability ( train_data )
print ("P( play tennis = No)" , prior_probablity[0])
print ("P( play tennis = Yes)" ,prior_probablity[1])

#4.3
train_data = create_train_data ()
_ , list_x_name = compute_conditional_probability ( train_data )
print ("x1 = ", list_x_name [0])
print ("x2 = ", list_x_name [1])
print ("x3 = ", list_x_name [2])
print ("x4 = ", list_x_name [3])

#4.4
train_data = create_train_data ()
_ , list_x_name = compute_conditional_probability ( train_data )
outlook = list_x_name [0]

i1 = get_index_from_value (" Overcast ", outlook )
i2 = get_index_from_value (" Rain ", outlook )
i3 = get_index_from_value (" Sunny ", outlook )
print ( i1 , i2 , i3 )



train_data = create_train_data ()
conditional_probability , list_x_name = compute_conditional_probability ( train_data )
# Compute P(" Outlook "=" Sunny "| Play Tennis "=" Yes ")
x1 = get_index_from_value (" Sunny ", list_x_name [0])
# Giả sử x1 là index của 'Sunny' trong list_x_name[0]
print("P('Outlook'='Sunny'|Play Tennis='Yes') = ", conditional_probability[0][x1][1])

train_data = create_train_data ()
conditional_probability , list_x_name = compute_conditional_probability ( train_data )
# Compute P(" Outlook "=" Sunny "| Play Tennis "=" No ")
x1 = get_index_from_value (" Sunny ", list_x_name [0])
print ("P(’Outlook’=’Sunny’|Play Tennis ’=’No’) = ", np . round ( conditional_probability[0][x1][0] ,2) )


X = ['Sunny','Cool', 'High', 'Strong']
data = create_train_data ()
prior_probability , conditional_probability , list_x_name = train_naive_bayes ( data )
pred = prediction_play_tennis (X , list_x_name , prior_probability ,
conditional_probability )
if( pred ) :
    print ("Ad should go!")
else :
    print ("Ad should not go!")