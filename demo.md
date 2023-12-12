---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Test notebook

Some Markdown.



```{code-cell} python

# Some code
print("hello")
```

+++ {"tags": ["code-cell-output"]}

hello

+++


```{code-cell} python

from jupyter_core.paths import jupyter_data_dir

jupyter_data_dir()
```




+++ {"tags": ["code-cell-output"]}

'/Users/tonyhirst/Library/Jupyter'

+++




```{code-cell} python

import numpy as np
import pandas as pd

np.random.seed(24)
df = pd.DataFrame({"A": np.linspace(1, 10, 10)})
df.plot()
```




+++ {"tags": ["code-cell-output"]}

<Axes: >

+++




    
```{image} data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAh8AAAGdCAYAAACyzRGfAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy81sbWrAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA6UklEQVR4nO3dd3xUdb7/8dfMpIckQCCBkAABQksgBWxgXVkURcVCSXCvunv37rqhiQ1c0UURsKFC0FUv666/JTQVFBVdRCkqSkmBUIO0QIBQM+ll5vz+0OUuigoymTPl/Xw85o+cmeS84yFz3n4/Z2YshmEYiIiIiLiJ1ewAIiIi4l9UPkRERMStVD5ERETErVQ+RERExK1UPkRERMStVD5ERETErVQ+RERExK1UPkRERMStAswO8H1Op5PS0lIiIiKwWCxmxxEREZFzYBgGFRUVxMXFYbX+9NqGx5WP0tJSEhISzI4hIiIiv0BJSQnx8fE/+RiPKx8RERHAt+EjIyNNTiMiIiLnwm63k5CQcPo8/lM8rnz8e9QSGRmp8iEiIuJlzuWSCV1wKiIiIm6l8iEiIiJupfIhIiIibuVx13ycC8MwaGxsxOFwmB2lydhsNgICAvRyYxER8TleVz7q6+s5dOgQ1dXVZkdpcmFhYbRt25agoCCzo4iIiLiMV5UPp9PJnj17sNlsxMXFERQU5JMrA4ZhUF9fz9GjR9mzZw9JSUk/+4YtIiIi3sKrykd9fT1Op5OEhATCwsLMjtOkQkNDCQwMZN++fdTX1xMSEmJ2JBEREZfwyv+d9pdVAH/5PUVExL/o7CYiIiJudd7lY/Xq1dx0003ExcVhsVhYsmTJGfcbhsFjjz1G27ZtCQ0NZcCAARQXF7sqr4iIiHi58y4fVVVVpKamMnv27LPe/8wzzzBz5kz++te/8vXXXxMeHs51111HbW3tBYcVERER73fe5WPQoEFMmTKFW2+99Qf3GYbBiy++yKOPPsott9xC7969efPNNyktLf3BCom/Wrt2LTabjRtvvNHsKCIiIqZw6TUfe/bs4fDhwwwYMOD0tqioKC655BLWrl171u+pq6vDbrefcfNlc+bMYfTo0axevZrS0lKz44iIiB+pbXAw8Z1NLNpQYmoOl77U9vDhwwDExsaesT02Nvb0fd83bdo0Jk+e/Iv3aRgGNQ3mvNNpaKDtvN5npLKykgULFrBhwwYOHz7M3//+dx555JEmTCgiIvKtXWWVjMrNY/vhCt4rKOXXPWNpHmbOm1ia/j4fEydOZPz48ae/ttvtJCQknPP31zQ46PnYx00R7WdtfeI6woLO/T/hwoUL6d69O926dePOO+9k3LhxTJw40SffKE1ERDzH2xsP8OiSImoaHLRqFsyLw9NMKx7g4rFLmzZtADhy5MgZ248cOXL6vu8LDg4mMjLyjJuvmjNnDnfeeScA119/PeXl5axatcrkVCIi4quq6xt5YFEh9y8qpKbBQb/O0Xw49nIuT2plai6XrnwkJibSpk0bVqxYQVpaGvDtSsbXX3/Nvffe68pdnRYaaGPrE9c1yc8+l32fqx07drBu3ToWL14MQEBAAMOHD2fOnDlcffXVTZRQRET81c4jFWTPzaO4rBKrBcYN6Er2NV2wWc1fbT/v8lFZWcmuXbtOf71nzx4KCgpo2bIl7du3Z9y4cUyZMoWkpCQSExOZNGkScXFxDBkyxJW5T7NYLOc1+jDLnDlzaGxsJC4u7vQ2wzAIDg4mJyeHqKgoE9OJiIivMAyDhRtKePy9LdQ2OImJCOalEelc1jna7GinnfdZe8OGDVxzzTWnv/739Rp33XUXf//733nooYeoqqrif/7nfzh16hSXX345H330kV9/NkljYyNvvvkmzz//PAMHDjzjviFDhjBv3jz++Mc/mpRORER8RWVdI48u3sySgm9fTXlFUiteGJ5Gq2bBJic7k8UwDMPsEP/JbrcTFRVFeXn5D67/qK2tZc+ePSQmJnpVmVmyZAnDhw+nrKzsByscDz/8MJ9++inr16//wfd56+8rIiLut7XUzqjcPHYfq8JmtXD/wK788crOWN00Zvmp8/f36bNd3GDOnDkMGDDgrKOV22+/nQ0bNrBp0yYTkomIiLczDIO5X+9jyMtfsPtYFW2jQpj/P5fyp6u7uK14nC/Pv1jCByxduvRH77v44ovxsMUnERHxEhW1DUx4ZzMfbDoEwK+6x/Dc0FRahpv3MtpzofIhIiLihYoOlpOdm8e+49UEWC08fH13fnd5oseudvwnlQ8REREvYhgGb67dx1MfbKPe4aRd81BmZaWT0b6F2dHOmcqHiIiIlyivaeDhtzbx0ZZvP7JkYM9Ynr0jlaiwQJOTnR+VDxERES9QUHKKUbl5HDhZQ6DNwiM39ODufh298iM6vLJ8+MsFmv7ye4qIyI8zDIM5n+/h6Y+20+AwaN8yjJysdHrHNzc72i/mVeUjMPDbZaXq6mpCQ0NNTtP0qqurgf/7vUVExL+cqq7ngUWFfLKtDIAberVh+u29iQzx7vOCV5UPm81G8+bNKSv79iCEhYV55XLTzzEMg+rqasrKymjevDk227l/hoyIiPiGjftOMDo3n9LyWoICrEwa3JM7L2nvE+c9ryof8H+fnPvvAuLLmjdv/qOfBiwiIr7J6TR4bc1unv14Bw6nQWKrcHKy0kmO853PAPO68mGxWGjbti0xMTE0NDSYHafJBAYGasVDRMTPHK+s4/5FhazccRSAm1PjmHpbL5oFe93p+id57W9js9l0chYREZ/x9e7jjJmfzxF7HcEBVibfnMzwixJ8YszyfV5bPkRERHyB02nw8spdzFi+E6cBnVuHM3tkBt3b/PSHs3kzlQ8RERGTHK2oY/zCAtYUHwPgtox2PHlLCuE+Nmb5Pt/+7URERDzUl7uOMXZBAUcr6ggNtPHELckM7Ztgdiy3UPkQERFxI4fTYOaKYmZ+WoxhQNfYZszOyiApNsLsaG6j8iEiIuImZfZaxszP56vdJwAY3jeBv9ycTGiQf72AQuVDRETEDVbvPMp9Cwo4XlVPWJCNqbf2Ykh6O7NjmULlQ0REpAk1Opy88MlOXl75DYYBPdpGMjsrnU6tm5kdzTQqHyIiIk3kUHkNY+bls37vSQBGXtKeSYN7EhLoX2OW71P5EBERaQKfbS9j/MICTlY30Cw4gOm392Jw7zizY3kElQ8REREXanA4ee7jHby6ejcAKe0imZ2VQYfocJOTeQ6VDxERERc5cLKa0fPyyd9/CoC7+3Vk4g3dCQ7w7zHL96l8iIiIuMC/thzmwbc2UV7TQERIAM/e0ZvrU9qaHcsjqXyIiIhcgPpGJ9OXbedvX+wBIDWhOTmZ6SS0DDM5medS+RAREfmFSk5UMyo3j8ID5QD89+WJPHR9d4ICrCYn82wqHyIiIr/Ass2HeOjtTVTUNhIVGsjzQ1MZ0DPW7FheQeVDRETkPNQ2OJj64TbeXLsPgD4dWjAzM512zUNNTuY9VD5ERETO0d5jVWTn5rGl1A7AH6/qzP0DuxJo05jlfKh8iIiInIP3Ckt55J3NVNY10jI8iBnDUrm6W4zZsbySyoeIiMhPqG1wMHnpVuat2w/AxYktmTkinTZRISYn814qHyIiIj9iV1klo3Lz2H64AosFRl3ThbHXJhGgMcsFUfkQERE5i3fyDvDokiKq6x20ahbEi8PTuTypldmxfILKh4iIyH+orm/k8Xe3sGjjAQD6dY7mxeFpxERqzOIqKh8iIiLf2Xmkguy5eRSXVWK1wNhruzLqV12wWS1mR/MpKh8iIuL3DMNg0cYDPPZuEbUNTmIignlpRDqXdY42O5pPUvkQERG/VlXXyKNLilicfxCAK5Ja8cLwNFo1CzY5me9S+RAREb+17ZCd7Ll57D5Whc1qYfyvu3LvVZ2xaszSpFQ+RETE7xiGQe66/UxeupX6RidtIkOYlZXORR1bmh3NL6h8iIiIX6mobWDiO5t5f9MhAK7p1prnh6XRMjzI5GT+Q+VDRET8RtHBckbl5rH3eDUBVgsPXd+N/768k8YsbqbyISIiPs8wDN5cu4+nPthGvcNJu+ahzMxMp0+HFmZH80sqHyIi4tPKaxqY8PYmlhUdBmBAj1ieG9qb5mEas5hF5UNERHxWYckpRs3Lo+REDYE2CxMH9eCe/h2xWDRmMZPKh4iI+BzDMPjbF3uZvmwbDQ6DhJah5GRmkJrQ3OxogsqHiIj4mFPV9TywaBOfbDsCwKCUNky/vTdRoYEmJ5N/U/kQERGfsXHfSUbn5lFaXkuQzcqkwT2489IOGrN4GJUPERHxek6nwWtrdvPsxztwOA06RoeRk5VBSrsos6PJWah8iIiIVztRVc/4hQWs3HEUgJtS45h6awoRIRqzeCqVDxER8Vrr9pxgzLx8DttrCQ6w8pebkxlxUYLGLB5O5UNERLyO02nw8spdzFi+E6cBnVqHMzsrgx5tI82OJudA5UNERLzK0Yo6xi8sYE3xMQBuS2/Hk0NSCA/WKc1b6EiJiIjX+HLXMcYuKOBoRR0hgVaeuCWFoX3iNWbxMiofIiLi8RxOg5kripn5aTGGAUkxzXh5ZAZJsRFmR5NfQOVDREQ8Wpm9lrHzC1i7+zgAw/rGM/nmFEKDbCYnk19K5UNERDzWmuKj3LeggGOV9YQF2Xjq1hRuTY83O5ZcIJUPERHxOI0OJy9+UszslbswDOjeJoKcrAy6xDQzO5q4gMqHiIh4lEPlNYydV8C6vScAyLqkPY8N7klIoMYsvkLlQ0REPMZn28sYv7CAk9UNNAsOYOptvbg5Nc7sWOJiKh8iImK6BoeT5z7ewaurdwOQHBfJ7KwMOrYKNzmZNAWVDxERMdXBUzWMzs0jb/8pAO66rAMTb+ihMYsPU/kQERHTLN96hAcWFVJe00BESADP3N6bQb3amh1LmpjKh4iIuF19o5Ppy7bzty/2AJAaH0VOVgYJLcNMTibuoPIhIiJuVXKimlG5eRQeKAfgd5cn8vD13QkKsJqcTNzF5Ufa4XAwadIkEhMTCQ0NpXPnzjz55JMYhuHqXYmIiJf5qOgQN8xcQ+GBcqJCA3n9v/oyaXBPFQ8/4/KVj6effppXXnmFf/zjHyQnJ7NhwwbuueceoqKiGDNmjKt3JyIiXqC2wcG0D7fxj7X7AMho35yZmenEt9CYxR+5vHx8+eWX3HLLLdx4440AdOzYkXnz5rFu3TpX70pERLzA3mNVZOfmsaXUDsAfrurEAwO7EWjTaoe/cvmR79evHytWrGDnzp0AFBYW8vnnnzNo0KCzPr6urg673X7GTUREfMPSwlIGz/qcLaV2WoQF8sbdFzFxUA8VDz/n8pWPCRMmYLfb6d69OzabDYfDwVNPPcXIkSPP+vhp06YxefJkV8cQERET1TY4mLx0K/PW7Qfgoo4tmJmZTtuoUJOTiSdweflYuHAhc+fOJTc3l+TkZAoKChg3bhxxcXHcddddP3j8xIkTGT9+/Omv7XY7CQkJro4lIiJu8s3RSrLn5rH9cAUWC2Rf3YVxA5II0GqHfMdiuPhlKAkJCUyYMIHs7OzT26ZMmcI///lPtm/f/rPfb7fbiYqKory8nMjISFdGExGRJrY4/wB/XlxEdb2D6PAgXhyRxhVJrc2OJW5wPudvl698VFdXY7We2W5tNhtOp9PVuxIREQ9RU+/gsXeLWLTxAACXdYrmpRFpxESGmJxMPJHLy8dNN93EU089Rfv27UlOTiY/P58ZM2bw29/+1tW7EhERD7DzSAXZc/MoLqvEYoExv0pizLVJ2KwWs6OJh3L52KWiooJJkyaxePFiysrKiIuLIzMzk8cee4ygoKCf/X6NXUREvINhGCzaeIDH3i2itsFJ64hgXhqeRr8urcyOJiY4n/O3y8vHhVL5EBHxfFV1jUxaUsQ7+QcBuCKpFTOGpdE6ItjkZGIWU6/5EBER37btkJ3s3Dx2H63CaoH7B3bj3qs6Y9WYRc6RyoeIiJwTwzCYt66EvyzdQn2jkzaRIczMTOfixJZmRxMvo/IhIiI/q6K2gUcWF7G0sBSAq7u1ZsawNFqG//y1fCLfp/IhIiI/qehgOaNy89h7vBqb1cJD13Xj91d00phFfjGVDxEROSvDMPh/X+1jyvvbqHc4iYsKYVZWBn06tDA7mng5lQ8REfmB8poGJry9iWVFhwEY0COW54b2pnmYxixy4VQ+RETkDIUlpxg1L4+SEzUE2ixMGNSD3/bviMWiMYu4hsqHiIgA345Z/vbFXqYv20aDwyC+RSizszJITWhudjTxMSofIiLCqep6Hli0iU+2HQHg+uQ2PH1Hb6JCA01OJr5I5UNExM9t3HeSMfPyOXiqhiCblUcH9+A3l3bQmEWajMqHiIifcjoNXl+zm2c/3kGj06BDdBizszJIaRdldjTxcSofIiJ+6ERVPfcvLOCzHUcBGNy7LdNu60VEiMYs0vRUPkRE/My6PScYMy+fw/ZaggKs/OWmZDIvTtCYRdxG5UNExE84nQavrPqGGct34nAadGodzuysDHq01SeIi3upfIiI+IFjlXXct6CANcXHALg1vR1ThqQQHqzTgLif/tWJiPi4L785xtj5BRytqCMk0MoTt6QwtE+8xixiGpUPEREf5XAazPq0mJkrinEakBTTjNkjM+gaG2F2NPFzKh8iIj6ozF7L2PkFrN19HIChfeKZfEsyYUF62hfz6V+hiIiPWVN8lPsWFHCssp6wIBtThqRwW0a82bFETlP5EBHxEY0OJy9+UszslbswDOjeJoKcrAy6xDQzO5rIGVQ+RER8wKHyGsbOK2Dd3hMAZF7cnsdv6klIoM3kZCI/pPIhIuLlPttRxvgFBZysbiA8yMa023tzc2qc2bFEfpTKh4iIl2pwOHnuXzt4ddVuAJLjIsnJyiCxVbjJyUR+msqHiIgXOniqhtG5eeTtPwXAf13WgUdu6KExi3gFlQ8RES+zfOsRHlhUSHlNAxEhATxze28G9WprdiyRc6byISLiJeobnTz90XbmfL4HgNT4KGZlZtA+OszkZCLnR+VDRMQLlJyoZlRuHoUHygH4bf9EJgzqTlCA1eRkIudP5UNExMN9VHSIB9/aREVtI5EhATw3NJWByW3MjiXyi6l8iIh4qLpGB1M/2MY/1u4DIL19c2ZlphPfQmMW8W4qHyIiHmjvsSpGzcuj6KAdgD9c1YkHBnYj0KYxi3g/lQ8REQ+ztLCUie9sprKukRZhgcwYlsY13WPMjiXiMiofIiIeorbBwRPvbyX36/0AXNSxBTMz02kbFWpyMhHXUvkQEfEA3xytJHtuHtsPV2CxwJ+u7sx9A7oSoDGL+CCVDxERky3OP8CfFxdRXe8gOjyIF4ancWXX1mbHEmkyKh8iIiapqXfw+HtFLNxwAIBLO7Vk5oh0YiJDTE4m0rRUPkRETFB8pII/zc2juKwSiwXG/CqJMdcmYbNazI4m0uRUPkRE3MgwDBZtPMBj7xZR2+CkdUQwLw1Po1+XVmZHE3EblQ8RETepqmtk0pIi3sk/CMAVSa2YMSyN1hHBJicTcS+VDxERN9h2yM6o3Dy+OVqF1QLjf92VP13dBavGLOKHVD5ERJqQYRjMW1fC5KVbqGt0EhsZzMwR6VzSKdrsaCKmUfkQEWkiFbUNPLK4iKWFpQBc3a01zw9NJbqZxizi31Q+RESaQNHBckbl5rH3eDU2q4UHr+vG/1zRSWMWEVQ+RERcyjAM/vnVPp58fxv1DidxUSHMykqnT4eWZkcT8RgqHyIiLmKvbWDC25v4cPNhAAb0iOG5oak0DwsyOZmIZ1H5EBFxgcKSU4yal0fJiRoCbRYevr47v7s8EYtFYxaR71P5EBG5AIZh8MYXe5m2bBsNDoP4FqHkZGWQltDc7GgiHkvlQ0TkFzpVXc+Db21i+dYjAFyf3Ian7+hNVGigyclEPJvKh4jIL5C3/ySjc/M5eKqGIJuVP9/Yg/+6rIPGLCLnQOVDROQ8OJ0G//v5bp75aAeNToMO0WHMzsogpV2U2dFEvIbKh4jIOTpRVc8Diwr5dHsZAIN7t2Xabb2ICNGYReR8qHyIiJyD9XtPMDo3n8P2WoICrDx+U0+yLm6vMYvIL6DyISLyE5xOg1dWfcOM5TtxOA06tQonJyuDnnGRZkcT8VoqHyIiP+JYZR33LShgTfExAG5Nb8eUISmEB+upU+RC6C9IROQs1n5znLHz8ymrqCMk0MoTN6cwtG+8xiwiLqDyISLyHxxOg5xPd/HSip04DUiKacbskRl0jY0wO5qIz1D5EBH5TllFLePmF/DlN8cBGNonnsm3JBMWpKdKEVfSX5SICPB58THGLcjnWGU9YUE2pgxJ4baMeLNjifgklQ8R8WuNDicvrSgm57NdGAZ0bxNBTlYGXWKamR1NxGepfIiI3zpcXsuY+fms23MCgMyL2/P4TT0JCbSZnEzEt6l8iIhfWrmjjPELCzlRVU94kI1pt/fm5tQ4s2OJ+AWVDxHxKw0OJ8//ayd/XfUNAMlxkeRkZZDYKtzkZCL+Q+VDRPxG6akaRs/LZ+O+kwD812UdeOSGHhqziLiZyoeI+IVPth7hgbcKOVXdQERwAE/f0ZsberU1O5aIX1L5EBGfVt/o5JmPtvO/n+8BoHd8FDmZGbSPDjM5mYj/sjbFDz148CB33nkn0dHRhIaG0qtXLzZs2NAUuxIR+VElJ6oZ+ura08Xjt/0TeeuP/VQ8REzm8pWPkydP0r9/f6655hqWLVtG69atKS4upkWLFq7elYjIj/qo6DAPvVWIvbaRyJAAnhuaysDkNmbHEhGaoHw8/fTTJCQk8MYbb5zelpiY6OrdiIicVV2jg2kfbufvX+4FIL19c2ZlphPfQqsdIp7C5WOX9957j759+zJ06FBiYmJIT0/n9ddf/9HH19XVYbfbz7iJiPwS+45Xcccra08Xjz9c2YmFf7hMxUPEw7i8fOzevZtXXnmFpKQkPv74Y+69917GjBnDP/7xj7M+ftq0aURFRZ2+JSQkuDqSiPiB9zeVcuPMz9l8sJwWYYH87e6+TLyhB4G2Jrm0TUQugMUwDMOVPzAoKIi+ffvy5Zdfnt42ZswY1q9fz9q1a3/w+Lq6Ourq6k5/bbfbSUhIoLy8nMjISFdGExEfVNvg4Mn3tzL36/0AXNSxBTMz02kbFWpyMhH/YrfbiYqKOqfzt8uv+Wjbti09e/Y8Y1uPHj14++23z/r44OBggoODXR1DRPzA7qOVZOfms+2QHYsF/nR1Z+4b0JUArXaIeDSXl4/+/fuzY8eOM7bt3LmTDh06uHpXIuLHluQf5JHFm6mudxAdHsQLw9O4smtrs2OJyDlwefm477776NevH1OnTmXYsGGsW7eO1157jddee83VuxIRP1RT7+Av721hwYYSAC7t1JKXRqQTGxlicjIROVcuv+YD4P3332fixIkUFxeTmJjI+PHj+f3vf39O33s+MyMR8S+7yirInpvPjiMVWCww5ldJjLk2CZvVYnY0Eb93PufvJikfF0LlQ0TO5q2NB5i0pIiaBgetI4J5aXga/bq0MjuWiHzH1AtORURcqbq+kUeXFPFO3kEALu/SiheGp9E6Qheqi3grlQ8R8VjbD9vJnpvHN0ersFpg/K+7cu/VXTRmEfFyKh8i4nEMw2DB+hIef28LdY1OYiODmTkinUs6RZsdTURcQOVDRDxKZV0jf168mXcLSgG4qmtrZgxLJbqZxiwivkLlQ0Q8xpbSckbl5rPnWBU2q4UHBnbjD1d2wqoxi4hPUfkQEdMZhsE/v97Pk+9vpb7RSVxUCLOy0unToaXZ0USkCah8iIip7LUNTHx7Mx9sPgTAgB4xPHtHKi3Cg0xOJiJNReVDREyz6cApRuXms/9ENQFWCxMGded3lydisWjMIuLLVD5ExO0Mw+DvX+5l6ofbaHAYxLcIJScrg7SE5mZHExE3UPkQEbcqr27gwbcK+dfWIwBclxzLM3ekEhUaaHIyEXEXlQ8RcZv8/ScZlZvPwVM1BNms/PnGHvzXZR00ZhHxMyofItLkDMPgf9fs4emPttPoNOgQHUZOZga94qPMjiYiJlD5EJEmdbKqngcWFbJiexkAN/Zuy7TbehEZojGLiL9S+RCRJrNh7wlGz8vnUHktQQFWHhvck5GXtNeYRcTPqXyIiMs5nQZ/Xf0Nz/9rJw6nQadW4eRkZdAz7qc/ZltE/IPKh4i41PHKOsYvLGTVzqMADEmLY8qtvWgWrKcbEfmWng1ExGW+2n2csfPzOWKvIyTQyuSbkxnWN0FjFhE5g8qHiFwwh9Ng9me7ePGTnTgN6BLTjNlZGXRrE2F2NBHxQCofInJByipquW9BAV/sOg7AHX3ieeKWZMKC9PQiImenZwcR+cW+2HWMsfMLOFZZR2igjSlDUri9T7zZsUTEw6l8iMh5czgNXvpkJ7M+24VhQLfYCGaPTKdLjMYsIvLzVD5E5LwcsdcyZl4+X+85AUDmxQk8flMyIYE2k5OJiLdQ+RCRc7Zq51HuW1DAiap6woNsTL2tF7ektTM7loh4GZUPEflZjQ4nzy/fySsrvwGgZ9tIcrLS6dS6mcnJRMQbqXyIyE8qPVXDmHn5bNh3EoDfXNqBP9/YQ2MWEfnFVD5E5Ed9uv0I4xcWcqq6gYjgAKbf3psbe7c1O5aIeDmVDxH5gQaHk2c+2s7ra/YA0KtdFDlZ6XSIDjc5mYj4ApUPETlDyYlqRs/Lp6DkFAD39O/IhEHdCQ7QmEVEXEPlQ0RO+3jLYR5cVIi9tpHIkACeHZrKdcltzI4lIj5G5UNEqGt0MH3Zdt74Yi8AaQnNmZWZTkLLMHODiYhPUvkQ8XP7jlcxKjefzQfLAfj9FYk8eF13ggKsJicTEV+l8iHixz7YdIgJb2+ioq6R5mGBPD80lWt7xJodS0R8nMqHiB+qbXAw5YOt/POr/QD07dCCmZnpxDUPNTmZiPgDlQ8RP7PnWBXZc/PYesgOwJ+u7sx9v+5KoE1jFhFxD5UPET/ybsFBHnlnM1X1DlqGB/HC8DSu6tra7Fgi4mdUPkT8QG2Dg7+8t4X560sAuCSxJTMz04mNDDE5mYj4I5UPER+3q6yC7Ln57DhSgcUCo3+VxJhfdSFAYxYRMYnKh4gPe2vjASYtKaKmwUGrZsG8NCKN/l1amR1LRPycyoeID6qub2TSki28nXcAgP5donlheBoxERqziIj5VD5EfMyOwxVk5+axq6wSqwXGDehK9jVdsFktZkcTEQFUPkR8hmEYLNxQwmPvbqGu0UlsZDAvjUjn0k7RZkcTETmDyoeID6isa+TRxZtZUlAKwJVdW/PCsFSimwWbnExE5IdUPkS83NZSO6Ny89h9rAqb1cL9A7vyxys7Y9WYRUQ8lMqHiJcyDIO5X+/nife3Ut/opG1UCLMy0+nbsaXZ0UREfpLKh4gXstc2MPGdzXyw6RAA13aP4bmhqbQIDzI5mYjIz1P5EPEymw+Uk52bx/4T1QRYLUwY1J3fXZ6IxaIxi4h4B5UPES9hGAb/+HIvUz/cTr3DSbvmoeRkpZPevoXZ0UREzovKh4gXKK9u4KG3C/l4yxEABvaM5dk7UokKCzQ5mYjI+VP5EPFw+ftPMnpePgdO1hBos/DIDT24u19HjVlExGupfIh4KMMwmPP5HqYv206j06B9yzBystLpHd/c7GgiIhdE5UPEA52squeBRYWs2F4GwI292jLt9l5EhmjMIiLeT+VDxMNs3HeC0bn5lJbXEhRg5bHBPRl5SXuNWUTEZ6h8iHgIp9Pg1dW7ee5fO3A4DRJbhZOTlU5yXJTZ0UREXErlQ8QDHK+sY/zCQlbtPArALWlxPHVrL5oF609URHyPntlETPb17uOMmZ/PEXsdwQFWnrglmWF9EzRmERGfpfIhYhKH0+Dlz3bxwic7cRrQuXU4L4/sQ7c2EWZHExFpUiofIiY4WlHHuAX5fLHrOAC3Z8Tz5JBkwoL0Jykivk/PdCJu9sWuY4ydX8CxyjpCA208OSSFO/rEmx1LRMRtVD5E3MThNHhpRTGzPi3GMKBbbAQ5WekkxWrMIiL+ReVDxA2O2GsZOz+fr3afAGDERQk8flMyoUE2k5OJiLifyodIE1u18yjjFxRwvKqe8CAbU2/rxS1p7cyOJSJiGpUPkSbS6HDy/PKdvLLyGwB6tI1kdlY6nVo3MzmZiIi5VD5EmkDpqRrGzMtnw76TANx5aXsevbEnIYEas4iIWJt6B9OnT8disTBu3Lim3pWIR/h0+xFumLmGDftOEhEcQE5WOlOG9FLxEBH5TpOufKxfv55XX32V3r17N+VuRDxCg8PJsx/v4LXVuwHo1S6KnKx0OkSHm5xMRMSzNNnKR2VlJSNHjuT111+nRYsWTbUbEY9w4GQ1Q/+69nTxuLtfR9669zIVDxGRs2iy8pGdnc2NN97IgAEDfvJxdXV12O32M24i3uRfWw5zw0trKCg5RWRIAK/+pg9/uTmZ4ACNWUREzqZJxi7z588nLy+P9evX/+xjp02bxuTJk5sihkiTqm90Mm3ZNt74Yi8AaQnNmZWZTkLLMHODiYh4OJevfJSUlDB27Fjmzp1LSEjIzz5+4sSJlJeXn76VlJS4OpKIy+0/Xs0df/3ydPH4/RWJLPzDZSoeIiLnwGIYhuHKH7hkyRJuvfVWbLb/W3J2OBxYLBasVit1dXVn3Pd9drudqKgoysvLiYyMdGU0EZf4cPMhHn5rExV1jTQPC+T5oalc2yPW7FgiIqY6n/O3y8cu1157LZs3bz5j2z333EP37t15+OGHf7J4iHiy2gYHT32wjf/31T4A+nZowczMdOKah5qcTETEu7i8fERERJCSknLGtvDwcKKjo3+wXcRb7DlWRfbcPLYe+vaC6Huv7sz4X3cl0Nbkb5UjIuJz9A6nIj/j3YKDPPLOZqrqHbQMD2LGsFSu7hZjdiwREa/llvKxcuVKd+xGxKVqGxxMXrqFeeu+vQj64sSWzByRTpuon7+QWkREfpxWPkTOYldZJdlz89hxpAKLBUZf04Ux1yYRoDGLiMgFU/kQ+Z63Nx7g0SVF1DQ4aNUsmBeHp3F5UiuzY4mI+AyVD5HvVNc38ti7W3hr4wEA+nWO5sURacREaMwiIuJKKh8iwM4jFWTPzaO4rBKrBcYN6Er2NV2wWS1mRxMR8TkqH+LXDMNg4YYSHn9vC7UNTmIigpmZmc6lnaLNjiYi4rNUPsRvVdY18ujizSwpKAXgyq6tmTEslVbNgk1OJiLi21Q+xC9tLbUzKjeP3ceqsFkt3D+wK3+8sjNWjVlERJqcyof4FcMwyF23n8lLt1Lf6KRtVAgzM9O5qGNLs6OJiPgNlQ/xGxW1DUx4ZzMfbDoEwK+6x/D80FRahAeZnExExL+ofIhfKDpYTnZuHvuOVxNgtfDw9d353eWJGrOIiJhA5UN8mmEYvLl2H099sI16h5N2zUOZlZVORvsWZkcTEfFbKh/is8prGnj4rU18tOUwAAN7xvLsHalEhQWanExExL+pfIhPKig5xajcPA6crCHQZuGRG3pwd7+OWCwas4iImE3lQ3yKYRjM+XwP05dtp9Fp0L5lGDlZ6fSOb252NBER+Y7Kh/iMU9X1PLCokE+2lQFwQ682TL+9N5EhGrOIiHgSlQ/xCRv3nWB0bj6l5bUEBViZNLgnd17SXmMWEREPpPIhXs3pNHhtzW6e/XgHDqdBYqtwcrLSSY6LMjuaiIj8CJUP8VrHK+u4f1EhK3ccBeDm1Dim3taLZsH6Zy0i4sn0LC1e6evdxxkzP58j9jqCA6xMvjmZ4RclaMwiIuIFVD7EqzidBi+v3MWM5TtxGtC5dTizR2bQvU2k2dFEROQcqXyI1zhaUcf4hQWsKT4GwG0Z7XjylhTCNWYREfEqetYWr/DlrmOMXVDA0Yo6QgNtPHFLMkP7JpgdS0REfgGVD/FoDqfBzBXFzPy0GMOArrHNmJ2VQVJshNnRRETkF1L5EI9VZq9lzPx8vtp9AoDhfRP4y83JhAbZTE4mIiIXQuVDPNLqnUe5b0EBx6vqCQuyMfXWXgxJb2d2LBERcQGVD/EojQ4nL3yyk5dXfoNhQI+2kczOSqdT62ZmRxMRERdR+RCPcai8hrHzCli399sxy8hL2jNpcE9CAjVmERHxJSof4hE+217G+IUFnKxuoFlwANNv78Xg3nFmxxIRkSag8iGmanA4ee7jHby6ejcAKe0iycnMoGOrcJOTiYhIU1H5ENMcPFXD6Nw88vafAuDufh2ZeEN3ggM0ZhER8WUqH2KKf205zINvbaK8poGIkACevaM316e0NTuWiIi4gcqHuFV9o5Ppy7bzty/2AJCa0JyczHQSWoaZnExERNxF5UPcpuRENaNy8yg8UA7Af1+eyEPXdycowGpyMhERcSeVD3GLZZsP8dDbm6iobSQqNJDnh6YyoGes2bFERMQEKh/SpGobHEz9cBtvrt0HQJ8OLZiZmU675qEmJxMREbOofEiT2XusiuzcPLaU2gH441WduX9gVwJtGrOIiPgzlQ9pEu8VlvLIO5uprGukZXgQzw9L5ZpuMWbHEhERD6DyIS5V2+Bg8tKtzFu3H4CLO7ZkZmY6baJCTE4mIiKeQuVDXGZXWSWjcvPYfrgCiwVGXdOFsdcmEaAxi4iI/AeVD3GJd/IO8OiSIqrrHbRqFsQLw9O4Iqm12bFERMQDqXzIBamub+Txd7ewaOMBAC7rFM1LI9KIidSYRUREzk7lQ36xnUcqyJ6bR3FZJVYLjL22K6N+1QWb1WJ2NBER8WAqH3LeDMNg0cYDPPZuEbUNTlpHBDNzRDqXdY42O5qIiHgBlQ85L1V1jTy6pIjF+QcBuCKpFS8MT6NVs2CTk4mIiLdQ+ZBztu2QnezcPHYfrcJqgfsHduPeqzpj1ZhFRETOg8qH/CzDMMhdt5/JS7dS3+ikTWQIMzPTuTixpdnRRETEC6l8yE+qqG1g4jubeX/TIQCu6daa54el0TI8yORkIiLirVQ+5EcVHSxnVG4ee49XE2C18ND13fjvyztpzCIiIhdE5UN+wDAM3ly7j6c+2Ea9w0m75qHMzEynT4cWZkcTEREfoPIhZyivaWDC25tYVnQYgAE9YnluaG+ah2nMIiIirqHyIacVlpxi1Lw8Sk7UEGizMHFQD+7p3xGLRWMWERFxHZUPwTAM/vbFXqYv20aDwyChZSg5mRmkJjQ3O5qIiPgglQ8/d6q6ngcWbeKTbUcAGJTShum39yYqNNDkZCIi4qtUPvzYxn0nGZ2bR2l5LUE2K48O7sFvLu2gMYuIiDQplQ8/5HQavLZmN89+vAOH06BjdBg5WRmktIsyO5qIiPgBlQ8/c6KqnvELC1i54ygAN6XGMfXWFCJCNGYRERH3UPnwI+v2nGDMvHwO22sJDrDy+E3JZF6coDGLiIi4lcqHH3A6DV5euYsZy3fiNKBT63BmZ2XQo22k2dFERMQPqXz4uKMVdYxfWMCa4mMA3JbejieHpBAerEMvIiLm0BnIh3256xhjFxRwtKKOkEArT9ySwtA+8RqziIiIqVQ+fJDDaTBzRTEzPy3GMCApphmzR2bQNTbC7GgiIiIqH76mzF7L2PkFrN19HIBhfeOZfHMKoUE2k5OJiIh8S+XDh6wpPsp9Cwo4VllPWJCNp25N4db0eLNjiYiInEHlwwc0Opy8+Ekxs1fuwjCge5sIcrIy6BLTzOxoIiIiP2B19Q+cNm0aF110EREREcTExDBkyBB27Njh6t3Idw6V15D1+tfkfPZt8ci6pD1LsvureIiIiMdyeflYtWoV2dnZfPXVVyxfvpyGhgYGDhxIVVWVq3fl9z7bXsYNL61h3d4TNAsOYGZmOlNv7UVIoK7vEBERz2UxDMNoyh0cPXqUmJgYVq1axZVXXvmzj7fb7URFRVFeXk5kpN4E62waHE6e+3gHr67eDUByXCSzszLo2Crc5GQiIuKvzuf83eTXfJSXlwPQsmXLs95fV1dHXV3d6a/tdntTR/JqB0/VMDo3j7z9pwC467IOTLyhh1Y7RETEazRp+XA6nYwbN47+/fuTkpJy1sdMmzaNyZMnN2UMn7F86xEeWFRIeU0DESEBPHN7bwb1amt2LBERkfPSpGOXe++9l2XLlvH5558TH3/2l3yebeUjISFBY5f/UN/oZPqy7fztiz0ApMZHMSszg/bRYSYnExER+ZZHjF1GjRrF+++/z+rVq3+0eAAEBwcTHBzcVDG8XsmJakbl5lF44Nvx1W/7JzJhUHeCAlx+rbCIiIhbuLx8GIbB6NGjWbx4MStXriQxMdHVu/AbHxUd4sG3NlFR20hUaCDPDU3l1z1jzY4lIiJyQVxePrKzs8nNzeXdd98lIiKCw4cPAxAVFUVoaKird+eTahscTPtwG/9Yuw+AjPbNmZmZTnwLjVlERMT7ufyajx/7xNQ33niDu++++2e/399farv3WBXZuXlsKf32VT9/uKoTDwzsRqBNYxYREfFcpl7z0cRvG+LTlhaWMvGdzVTWNdIiLJAZw9K4pnuM2bFERERcSp/t4gFqGxw88f5Wcr/eD8BFHVswMzOdtlEaU4mIiO9R+TDZN0cryZ6bx/bDFVgskH11F8YNSCJAYxYREfFRKh8mWpx/gD8vLqK63kF0eBAvjkjjiqTWZscSERFpUiofJqipd/D4e0Us3HAAgMs6RfPSiDRiIkNMTiYiItL0VD7cbOeRCrLn5lFcVonFAmOvTWL0r5KwWc/+KiERERFfo/LhJoZhsGjjAR57t4jaBietI4J5aUQa/Tq3MjuaiIiIW6l8uEFVXSOTlhTxTv5BAK5IasWMYWm0jtDbyouIiP9R+Whi2w7Zyc7NY/fRKqwWuH9gN+69qjNWjVlERMRPqXw0EcMwmLeuhMlLt1DX6KRNZAgzM9O5OLGl2dFERERMpfLRBCpqG3hkcRFLC0sBuLpba2YMS6NleJDJyURERMyn8uFiRQfLGZWbx97j1disFh66rhu/v6KTxiwiIiLfUflwEcMw+H9f7WPK+9uodzhp1zyUmZnp9OnQwuxoIiIiHkXlwwXKaxqY+M4mPtx8GIABPWJ5bmhvmodpzCIiIvJ9Kh8XqLDkFKPm5VFyooZAm4UJg3rw2/4dsVg0ZhERETkblY9fyDAM/vbFXqYv20aDwyC+RSizszJITWhudjQRERGPpvLxC5yqrueBRZv4ZNsRAK5PbsPTd/QmKjTQ5GQiIiKeT+XjPG3cd5Ix8/I5eKqGIJuVRwf34DeXdtCYRURE5BypfJwjp9Pg9TW7efbjHTQ6DTpEhzE7K4OUdlFmRxMREfEqKh/n4ERVPfcvLOCzHUcBGNy7LdNu60VEiMYsIiIi50vl42es23OCMfPyOWyvJSjAyl9uSibz4gSNWURERH4hlY8f4XQavLLqG2Ys34nDadCpdTizszLo0TbS7GgiIiJeTeXjLI5V1nHfggLWFB8D4Nb0dkwZkkJ4sP5ziYiIXCidTb9n7TfHGTs/n7KKOkICrTxxSwpD+8RrzCIiIuIiKh/fcTgNZn1azMwVxTgNSIppxuyRGXSNjTA7moiIiE9R+QDK7LWMW1DAl98cB2BY33gm35xCaJDN5GQiIiK+x+/Lx5rio9y3oIBjlfWEBdmYMiSF2zLizY4lIiLis/y2fDQ6nLz4STGzV+7CMKB7mwhysjLoEtPM7GgiIiI+zS/Lx+HyWsbMy2fd3hMAZF3SnscG9yQkUGMWERGRpuZ35eOzHWXcv7CQE1X1NAsOYOptvbg5Nc7sWCIiIn7Db8pHg8PJc//awaurdgOQHBfJ7KwMOrYKNzmZiIiIf/Gb8rFi25HTxeOuyzow8YYeGrOIiIiYwG/Kx3XJbbjz0vb079yKQb3amh1HRETEb/lN+bBYLEwZ0svsGCIiIn7PanYAERER8S8qHyIiIuJWKh8iIiLiViofIiIi4lYqHyIiIuJWKh8iIiLiViofIiIi4lYqHyIiIuJWKh8iIiLiViofIiIi4lYqHyIiIuJWKh8iIiLiViofIiIi4lYe96m2hmEAYLfbTU4iIiIi5+rf5+1/n8d/iseVj4qKCgASEhJMTiIiIiLnq6KigqioqJ98jMU4l4riRk6nk9LSUiIiIrBYLC792Xa7nYSEBEpKSoiMjHTpz5bzp+PhWXQ8PIuOh+fRMflphmFQUVFBXFwcVutPX9XhcSsfVquV+Pj4Jt1HZGSk/uF4EB0Pz6Lj4Vl0PDyPjsmP+7kVj3/TBaciIiLiViofIiIi4lZ+VT6Cg4N5/PHHCQ4ONjuKoOPhaXQ8PIuOh+fRMXEdj7vgVERERHybX618iIiIiPlUPkRERMStVD5ERETErVQ+RERExK38pnzMnj2bjh07EhISwiWXXMK6devMjuS3pk2bxkUXXURERAQxMTEMGTKEHTt2mB1LvjN9+nQsFgvjxo0zO4rfOnjwIHfeeSfR0dGEhobSq1cvNmzYYHYsv+RwOJg0aRKJiYmEhobSuXNnnnzyyXP6/BL5cX5RPhYsWMD48eN5/PHHycvLIzU1leuuu46ysjKzo/mlVatWkZ2dzVdffcXy5ctpaGhg4MCBVFVVmR3N761fv55XX32V3r17mx3Fb508eZL+/fsTGBjIsmXL2Lp1K88//zwtWrQwO5pfevrpp3nllVfIyclh27ZtPP300zzzzDPMmjXL7GhezS9eanvJJZdw0UUXkZOTA3z7+TEJCQmMHj2aCRMmmJxOjh49SkxMDKtWreLKK680O47fqqysJCMjg5dffpkpU6aQlpbGiy++aHYsvzNhwgS++OIL1qxZY3YUAQYPHkxsbCxz5sw5ve32228nNDSUf/7znyYm824+v/JRX1/Pxo0bGTBgwOltVquVAQMGsHbtWhOTyb+Vl5cD0LJlS5OT+Lfs7GxuvPHGM/5WxP3ee+89+vbty9ChQ4mJiSE9PZ3XX3/d7Fh+q1+/fqxYsYKdO3cCUFhYyOeff86gQYNMTubdPO6D5Vzt2LFjOBwOYmNjz9geGxvL9u3bTUol/+Z0Ohk3bhz9+/cnJSXF7Dh+a/78+eTl5bF+/Xqzo/i93bt388orrzB+/HgeeeQR1q9fz5gxYwgKCuKuu+4yO57fmTBhAna7ne7du2Oz2XA4HDz11FOMHDnS7GhezefLh3i27OxsioqK+Pzzz82O4rdKSkoYO3Ysy5cvJyQkxOw4fs/pdNK3b1+mTp0KQHp6OkVFRfz1r39V+TDBwoULmTt3Lrm5uSQnJ1NQUMC4ceOIi4vT8bgAPl8+WrVqhc1m48iRI2dsP3LkCG3atDEplQCMGjWK999/n9WrVxMfH292HL+1ceNGysrKyMjIOL3N4XCwevVqcnJyqKurw2azmZjQv7Rt25aePXuesa1Hjx68/fbbJiXybw8++CATJkxgxIgRAPTq1Yt9+/Yxbdo0lY8L4PPXfAQFBdGnTx9WrFhxepvT6WTFihVcdtllJibzX4ZhMGrUKBYvXsynn35KYmKi2ZH82rXXXsvmzZspKCg4fevbty8jR46koKBAxcPN+vfv/4OXnu/cuZMOHTqYlMi/VVdXY7Weeaq02Ww4nU6TEvkGn1/5ABg/fjx33XUXffv25eKLL+bFF1+kqqqKe+65x+xofik7O5vc3FzeffddIiIiOHz4MABRUVGEhoaanM7/RERE/OB6m/DwcKKjo3Udjgnuu+8++vXrx9SpUxk2bBjr1q3jtdde47XXXjM7ml+66aabeOqpp2jfvj3Jycnk5+czY8YMfvvb35odzbsZfmLWrFlG+/btjaCgIOPiiy82vvrqK7Mj+S3grLc33njD7GjynauuusoYO3as2TH81tKlS42UlBQjODjY6N69u/Haa6+ZHclv2e12Y+zYsUb79u2NkJAQo1OnTsaf//xno66uzuxoXs0v3udDREREPIfPX/MhIiIinkXlQ0RERNxK5UNERETcSuVDRERE3ErlQ0RERNxK5UNERETcSuVDRERE3ErlQ0RERNxK5UNERETcSuVDRERE3ErlQ0RERNxK5UNERETc6v8DhMNG86uIctQAAAAASUVORK5CYII=
```

