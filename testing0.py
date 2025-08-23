{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "1f128e3d-8e41-4d2f-8722-f1fe0027f2e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "93ef0c19-9178-4cc0-9d73-6b3bd97bbd1d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: []\n",
       "Index: []"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame()\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "1927b41b-9ca5-47a6-ac0a-060b7ea46255",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 0 entries\n",
      "Empty DataFrame\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "6e3a506c-7219-444e-94e5-e6d7f6136555",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Texus', 'Claforniiya', 'Slicon Vali']"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city = ['Texus', 'Claforniiya', 'Slicon Vali']\n",
    "city"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "db2b1ebe-622b-4fe6-aa62-d98771c22c07",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(city)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "e81de336-27c6-43e9-bdae-3c580ae54fa4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Texus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Claforniiya</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Slicon Vali</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             0\n",
       "0        Texus\n",
       "1  Claforniiya\n",
       "2  Slicon Vali"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "4d5a3664-83c4-4444-8d51-5c43cffc902c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "2f539b4b-9619-4b1f-9729-2caaf4e160e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(city)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "ea85789b-224e-4c16-a278-718049bc9c03",
   "metadata": {},
   "outputs": [],
   "source": [
    "row, col = df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "321b71f6-74aa-4974-b857-cb382affe436",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "2ab1545e-acd5-4a3d-8a9f-13372de5e260",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "col"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "f33724b5-a5df-4760-ad46-0dd5e48ae2c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 1)"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "fb83f649-c12d-4f76-a0b4-f9f7caf56100",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 1)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "f224d529-9d96-453b-a846-c918b4570b81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 1)"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "row, col"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "05902995-7d67-4fbe-b99a-69878c4f8367",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Texus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Claforniiya</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Slicon Vali</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             0\n",
       "0        Texus\n",
       "1  Claforniiya\n",
       "2  Slicon Vali"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "1bf55f4a-d140-4f67-99fe-82341122d9f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>city_in_usa</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Texus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Claforniiya</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Slicon Vali</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   city_in_usa\n",
       "0        Texus\n",
       "1  Claforniiya\n",
       "2  Slicon Vali"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(city, columns=['city_in_usa'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "02b0fa88-2341-41eb-8140-643b7765c63e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>city_in_texus</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>c1</th>\n",
       "      <td>Texus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c2</th>\n",
       "      <td>Claforniiya</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c3</th>\n",
       "      <td>Slicon Vali</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   city_in_texus\n",
       "c1         Texus\n",
       "c2   Claforniiya\n",
       "c3   Slicon Vali"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(city, columns=['city_in_texus'], index=['c1', 'c2', 'c3'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "293f7dd3-ff19-4e63-879d-e725dea33330",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>city1</th>\n",
       "      <th>city2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Texus</td>\n",
       "      <td>Vatican_city</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Claforniiya</td>\n",
       "      <td>parise</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Slicon Vali</td>\n",
       "      <td>lexumbarg</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         city1         city2\n",
       "0        Texus  Vatican_city\n",
       "1  Claforniiya        parise\n",
       "2  Slicon Vali     lexumbarg"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2 = ['Vatican_city', 'parise', 'lexumbarg']\n",
    "df2 = pd.DataFrame(zip(city, city2), columns=['city1', 'city2'])\n",
    "df2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "8e84e278-d593-4d0b-8dda-fa2eb4b73d68",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 1)"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "580a171e-849f-4d41-9454-1849d58be3ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 1)"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "row, col"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "c5502217-af3e-4e10-9786-c6d8514a5770",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 2)"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.shape\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "a0698fbc-8bd2-4f2c-87cf-a7c2d7600853",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['Bravo', 'Australia'], ['BMW', 'DUWR']]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city3 = [['Bravo', 'Australia'], ['BMW', 'DUWR']]\n",
    "city3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "455ac3b7-b0f8-4477-b42c-7321e70f4d14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>State</th>\n",
       "      <th>City</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Bravo</td>\n",
       "      <td>Australia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>BMW</td>\n",
       "      <td>DUWR</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   State       City\n",
       "0  Bravo  Australia\n",
       "1    BMW       DUWR"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df4 = pd.DataFrame(city3, columns=['State', 'City'])\n",
    "df4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "5e10128d-0bac-4b2b-b62c-85b259c9c21f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Texus', 'Claforniiya', 'Slicon Vali']"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "cbeca891-5a6d-4243-a5bd-ddcf36c19072",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Vatican_city', 'parise', 'lexumbarg']"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "69bc1fbc-37c0-45d5-8d91-7d14199ecd71",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict1 = {\n",
    "    'city1': city,\n",
    "    'city2': city2,\n",
    "    \n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "865ebb44-0635-4f51-a4ce-e6d899fbf335",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'city1': ['Texus', 'Claforniiya', 'Slicon Vali'],\n",
       " 'city2': ['Vatican_city', 'parise', 'lexumbarg']}"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "3cb9fd87-dc17-4881-9942-76f853c96b9a",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unterminated string literal (detected at line 1) (2332111083.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[65], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    df = pd.read_csv(time text2.csv')\u001b[0m\n\u001b[1;37m                                   ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unterminated string literal (detected at line 1)\n"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv(time text2.csv')\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b656859-2812-4e2a-b25c-b0295dafca37",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
