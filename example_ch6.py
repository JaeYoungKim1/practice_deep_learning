# import numpy as np
# samples = ['The cat sat on the mat.', 'The dog ate my homework.']
# token_index = {}
# for sample in samples:
#     for word in sample.split():
#         if word not in token_index:
#             token_index[word] = len(token_index) + 1
# max_length = 10
# results = np.zeros(shape=(len(samples), max_length, max(token_index.values()) + 1))
# for i, sample in enumerate(samples):
#     for j, word in list(enumerate(sample.split()))[:max_length]:
#         index = token_index.get(word)
#         results[i, j, index] = 1.
# print(results)


# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Embedding, Flatten, Dense
#
# model = Sequential()
# model.add(Embedding(max_words, embedding_dim, input_length=maxlen))
# model.add(Flatten())
# model.add(Dense(32, activation = 'relu'))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()
# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
#
# history = model.fit(x_train, y_train, epochs = 10, batch_size = 32, validation_data = (x_val, y_val))


from tensorflow.keras.preprocessing.text import Tokenizer

samples = ['The cat sat on the mat.', 'The dog ate my homework.']

tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(samples)

sequences = tokenizer.texts_to_sequences(samples)

one_hot_results = tokenizer.texts_to_matrix(samples, mode='binary')
word_index = tokenizer.word_index
print('%s개의 고유한 토근을 찾았습니다.' % len(word_index))