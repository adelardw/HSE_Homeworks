import numpy as np
from sklearn.model_selection import train_test_split
import copy
from typing import NoReturn

# Task 1

class Perceptron:
    def __init__(self, iterations: int = 100):
        """
        Parameters
        ----------
        iterations : int
        Количество итераций обучения перцептрона.

        Attributes
        ----------
        w : np.ndarray
        Веса перцептрона размерности X.shape[1] + 1 (X --- данные для обучения), 
        w[0] должен соответстовать константе, 
        w[1:] - коэффициентам компонент элемента X.

        Notes
        -----
        Вы можете добавлять свои поля в класс.
        
        """

        self.w = None
        self.iterations = iterations
    
    def fit(self, X: np.ndarray, y: np.ndarray) -> NoReturn:
        """
        Обучает простой перцептрон. 
        Для этого сначала инициализирует веса перцептрона,
        а затем обновляет их в течении iterations итераций.
        
        Parameters
        ----------
        X : np.ndarray
            Набор данных, на котором обучается перцептрон.
        y: np.ndarray
            Набор меток классов для данных.
        
        """

        self.w = np.zeros(X.shape[1] + 1)
        
        thshld = np.ones(X.shape[0]).reshape(-1,1)
        X = np.hstack((thshld,X))
        self.uniq = np.unique(y)
        y_cop = np.copy(y)

        y_cop[y_cop == self.uniq[0]] = -1
        
        for i in range(self.iterations):
            
            arg = y_cop != np.sign( X @ self.w)
            self.w += y_cop[arg] @ X [arg]
            if len(X[arg]) == 0:
               break

        
            
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Предсказывает метки классов.
        
        Parameters
        ----------
        X : np.ndarray
            Набор данных, для которого необходимо вернуть метки классов.
        
        Return
        ------
        labels : np.ndarray
            Вектор индексов классов 
            (по одной метке для каждого элемента из X).
        
        """

        thshld = np.ones(X.shape[0]).reshape(-1,1)
        X = np.hstack((thshld,X))

        y_pred = np.sign(X @ self.w)
        y_pred[y_pred == -1] = 0

        return y_pred
    
# Task 2

class PerceptronBest:

    def __init__(self, iterations: int = 100):
        """
        Parameters
        ----------
        iterations : int
        Количество итераций обучения перцептрона.

        Attributes
        ----------
        w : np.ndarray
        Веса перцептрона размерности X.shape[1] + 1 (X --- данные для обучения), 
        w[0] должен соответстовать константе, 
        w[1:] - коэффициентам компонент элемента X.

        Notes
        -----
        Вы можете добавлять свои поля в класс.
        

        """

        self.w = None
        self.iterations = iterations
    
    def fit(self, X: np.ndarray, y: np.ndarray) -> NoReturn:
        """
        Обучает перцептрон.

        Для этого сначала инициализирует веса перцептрона, 
        а затем обновляет их в течении iterations итераций.

        При этом в конце обучения оставляет веса, 
        при которых значение accuracy было наибольшим.
        
        Parameters
        ----------
        X : np.ndarray
            Набор данных, на котором обучается перцептрон.
        y: np.ndarray
            Набор меток классов для данных.
        
        """

        self.w = np.zeros(X.shape[1] + 1)
        
        thshld = np.ones(X.shape[0]).reshape(-1,1)
        X = np.hstack((thshld,X))


        y_cop = y.copy()
        y_cop[y_cop == 0] = -1
        best_ac = -1

        
        for i in range(self.iterations):
            
            arg = y_cop != np.sign( X @ self.w)
            self.w += y_cop[arg] @ X [arg]

            y_pred = np.sign(X @ self.w)
            acc = np.sum(y_pred == y_cop)/len(y_pred)
            if acc > best_ac:
                best_ac = acc
                self.best_w = self.w.copy()
            
            if len(X[arg]) == 0:
               break

            
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Предсказывает метки классов.
        
        Parameters
        ----------
        X : np.ndarray
            Набор данных, для которого необходимо вернуть метки классов.
        
        Return
        ------
        labels : np.ndarray
            Вектор индексов классов 
            (по одной метке для каждого элемента из X).
        
        """
        thshld = np.ones(X.shape[0]).reshape(-1,1)
        X = np.hstack((thshld,X))
        y_pred = np.sign(X @ self.best_w)
        y_pred[y_pred == -1] = 0
        return y_pred
    
# Task 3




def transform_images(images: np.ndarray) -> np.ndarray:
    """
    Переводит каждое изображение в вектор из двух элементов.
        
    Parameters
    ----------
    images : np.ndarray
        Трехмерная матрица с черное-белыми изображениями.
        Её размерность: (n_images, image_height, image_width).

    Return
    ------
    np.ndarray
        Двумерная матрица с преобразованными изображениями.
        Её размерность: (n_images, 2).
    """
    #return np.zeros((images.shape[0], 2))

    result = np.zeros((images.shape[0], 2))
    h_sym = np.zeros(images.shape[0])  #horizontal symmetry
    v_sym = np.zeros(images.shape[0])  #vertical symmetry

    for i in range(images.shape[0]):
        h_sym[i] = np.mean(np.abs(images[i] - images[i][:, ::-1]))
        v_sym[i] = np.mean(np.abs(images[i] - images[i][::-1]))


    result[:, 0] = h_sym
    result[:, 1] = v_sym

    return result

