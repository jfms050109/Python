import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import threading

# Define os dados de entrada (padrões de letras)
inputs = np.random.randint(0, 2, size=(100, 5, 5))

# Define as respostas esperadas (identificar as letras 'A' ou 'B')
labels = np.array(['A', 'B'])[np.random.randint(0, 2, size=100)]

# Cria o modelo de rede neural
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(5, 5)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])

# Compila o modelo com a função de perda e o otimizador
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Define uma função para treinar o modelo em uma thread separada
def train_model(model, x, y):
    model.fit(x, y, epochs=10, verbose=0)

# Cria uma lista de threads para treinar os modelos
threads = []
for i in range(100):
    # Cria um novo modelo para cada thread
    new_model = tf.keras.models.clone_model(model)
    new_model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    # Cria uma nova thread para treinar o modelo
    t = threading.Thread(target=train_model, args=(new_model, inputs[i], labels[i]))
    threads.append(t)
    t.start()

# Espera todas as threads terminarem
for t in threads:
    t.join()

# Avalia a precisão de cada modelo treinado
accuracies = []
for i in range(100):
    accuracies.append(model.evaluate(inputs[i], [labels[i]], verbose=0)[1])

# Plota um gráfico com as precisões dos modelos
plt.hist(accuracies, bins=10, range=(0, 1))
plt.title('Precisões das Inteligências Artificiais')
plt.xlabel('Precisão')
plt.ylabel('Número de Modelos')
plt.show()
