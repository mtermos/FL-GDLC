from keras import layers, models, Input, regularizers, optimizers


def CNNLSTM(input_shape, alpha=0.001, LAMBD_2=0.001, num_classes=2):
    model = models.Sequential()

    model.add(layers.Conv1D(80, kernel_size=3,
                            activation="relu", input_shape=(input_shape, 1), kernel_regularizer=regularizers.L2(l2=LAMBD_2)))
    model.add(layers.MaxPooling1D())
    model.add(layers.LayerNormalization(axis=1))
    model.add(layers.Dropout(0.3))
    # .L1L2(l1=LAMBD_1, l2=LAMBD_2)
    model.add(layers.Conv1D(80, 3, activation='relu',
              kernel_regularizer=regularizers.L2(l2=LAMBD_2)))
    model.add(layers.MaxPooling1D())
    model.add(layers.LayerNormalization(axis=1))
    model.add(layers.Dropout(0.3))

    # model.add(layers.LSTM(units=80,
    #                         activation='relu',
    #                         kernel_regularizer=regularizers.L1L2(l1=LAMBD_1, l2=LAMBD_2),
    #                         recurrent_regularizer=regularizers.L1L2(l1=LAMBD_1, l2=LAMBD_2),
    #                         bias_regularizer=regularizers.L1L2(l1=LAMBD_1, l2=LAMBD_2),
    #                         return_sequences=False,
    #                         ))
    # model.add(layers.LayerNormalization(axis=1))

    model.add(layers.Flatten())

    model.add(layers.Dense(200, activation='relu',
              kernel_regularizer=regularizers.L2(l2=LAMBD_2)))
    model.add(layers.LayerNormalization(axis=1))
    model.add(layers.Dropout(0.1))
    model.add(layers.Dense(200, activation='relu',
              kernel_regularizer=regularizers.L2(l2=LAMBD_2)))
    model.add(layers.LayerNormalization(axis=1))
    model.add(layers.Dropout(0.1))
    model.add(layers.Dense(80, activation='relu',
              kernel_regularizer=regularizers.L2(l2=LAMBD_2)))
    model.add(layers.LayerNormalization(axis=1))
    model.add(layers.Dropout(0.1))

    if num_classes > 2:
        model.add(layers.Dense(num_classes, activation='softmax'))
        model.compile(optimizer=optimizers.Adam(learning_rate=alpha),
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
    else:
        model.add(layers.Dense(1, activation='sigmoid'))
        model.compile(optimizer=optimizers.Adam(learning_rate=alpha),
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

    return model
