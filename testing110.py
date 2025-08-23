{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ca02a165-4fbd-47fb-8b5c-6748834b03cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "91763eb5-b41f-4c9a-8b69-9141d1504c42",
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
     "execution_count": 2,
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
   "execution_count": 3,
   "id": "dca3a335-53a5-47be-a871-367a76ca60be",
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
   "execution_count": 8,
   "id": "bddebe97-0206-4e42-96d5-dfc8031d79bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "city = ['texus', 'clafornia', 'valicon city']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3fd29d6e-8a03-4fa7-bd5d-ba31bcb0eb4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(city)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e07056ef-f39f-4303-827b-0b8a1ca0c302",
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
       "      <td>texus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>clafornia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>valicon city</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              0\n",
       "0         texus\n",
       "1     clafornia\n",
       "2  valicon city"
      ]
     },
     "execution_count": 6,
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
   "execution_count": 10,
   "id": "90f69db5-4cba-4489-a4d3-2faf42d55e6a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 10,
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
   "execution_count": 11,
   "id": "797bb91f-67b7-4b6e-bcbb-3794a915dd5a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 11,
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
   "execution_count": 14,
   "id": "0bf6cb5b-a902-472a-8dba-536fbd26e5ab",
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
       "      <td>texus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>clafornia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>valicon city</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              0\n",
       "0         texus\n",
       "1     clafornia\n",
       "2  valicon city"
      ]
     },
     "execution_count": 14,
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
   "execution_count": 17,
   "id": "e77d2dc4-a4e6-4932-89d8-b4c1f3cb3dfe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 17,
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
   "execution_count": 18,
   "id": "39a1f76c-1091-4df3-b56f-d94dca1dd687",
   "metadata": {},
   "outputs": [],
   "source": [
    "row, col = df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "afa52663-e046-4198-b8c9-d62b337003af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 19,
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
   "execution_count": 20,
   "id": "b7947029-77d6-473a-ac39-6a4fb6c6a71e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 20,
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
   "execution_count": 21,
   "id": "1f07d01f-e56f-4cd6-8848-8d75d4876049",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 1)"
      ]
     },
     "execution_count": 21,
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
   "execution_count": 23,
   "id": "42f17581-584a-4aca-9665-2bc3aa8a305d",
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
       "      <th>city_in_USA</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>texus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>clafornia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>valicon city</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    city_in_USA\n",
       "0         texus\n",
       "1     clafornia\n",
       "2  valicon city"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(city, columns=['city_in_USA'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "2c1d4ed4-06ae-4f3d-9c90-7db77c8c98e1",
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
       "      <th>City_in_Europe</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>c1</th>\n",
       "      <td>texus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c2</th>\n",
       "      <td>clafornia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c3</th>\n",
       "      <td>valicon city</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   City_in_Europe\n",
       "c1          texus\n",
       "c2      clafornia\n",
       "c3   valicon city"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(city, columns=['City_in_Europe'], index=['c1', 'c2', 'c3'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "32936217-b817-4948-b825-26c01ab07892",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 1)"
      ]
     },
     "execution_count": 25,
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
   "execution_count": 55,
   "id": "be110699-a04b-49ca-bbf7-f42369dcf82d",
   "metadata": {},
   "outputs": [],
   "source": [
    "town = ['vatican_city', 'texus', 'hollywood']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "5776f9bb-7b56-41c1-8161-6d497b3bc81c",
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
       "      <td>vatican_city</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>texus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>hollywood</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              0\n",
       "0  vatican_city\n",
       "1         texus\n",
       "2     hollywood"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2 = pd.DataFrame(town)\n",
    "df2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "cae0c04c-39fe-49c6-b2ef-f1aa373f05a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df2 = pd.DataFrame(town, columns=['City_in_Texus'], index=['City1', 'City2', 'City3'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "d17c46aa-7566-4978-aefd-86bbe33b609a",
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
       "      <th>City_in_Texus</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>City1</th>\n",
       "      <td>vatican_city</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>City2</th>\n",
       "      <td>texus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>City3</th>\n",
       "      <td>hollywood</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      City_in_Texus\n",
       "City1  vatican_city\n",
       "City2         texus\n",
       "City3     hollywood"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "00cae6dc-76d0-4ad1-b9bd-25d6ca8be55c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df3 = pd.DataFrame(zip(city, town), columns=['USA', 'UA'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "f2eb72c1-4008-4200-95ba-ec73737ce9ff",
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
       "      <th>USA</th>\n",
       "      <th>UA</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>texus</td>\n",
       "      <td>vatican_city</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>clafornia</td>\n",
       "      <td>texus</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>valicon city</td>\n",
       "      <td>hollywood</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            USA            UA\n",
       "0         texus  vatican_city\n",
       "1     clafornia         texus\n",
       "2  valicon city     hollywood"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "97485128-6b89-418f-ae6f-d477e99785eb",
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
    " df3.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "cc6808c7-83ff-41ff-ad4b-3aa28d3ed0b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "town3 = [['Bravia', 'England'], ['Neuziland', 'Biyetname'], ['hawzu', 'khauzo']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "4b71cc8d-41b7-476a-ae30-a1402bac37d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "df4 = pd.DataFrame(town3, columns=['state', 'stats'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "3ff4c8da-a86a-4b71-a286-3762db1144d2",
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
       "      <th>state</th>\n",
       "      <th>stats</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Bravia</td>\n",
       "      <td>England</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Neuziland</td>\n",
       "      <td>Biyetname</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>hawzu</td>\n",
       "      <td>khauzo</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       state      stats\n",
       "0     Bravia    England\n",
       "1  Neuziland  Biyetname\n",
       "2      hawzu     khauzo"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "82aed0a1-2144-49c5-a463-08769645c9bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "df5 = pd.DataFrame(town3, columns=['Faver', 'look'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "63038398-eb58-4941-97cf-dee937f661fd",
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
       "      <th>Faver</th>\n",
       "      <th>look</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Bravia</td>\n",
       "      <td>England</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Neuziland</td>\n",
       "      <td>Biyetname</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>hawzu</td>\n",
       "      <td>khauzo</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Faver       look\n",
       "0     Bravia    England\n",
       "1  Neuziland  Biyetname\n",
       "2      hawzu     khauzo"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "98681da5-68b8-4e83-99b4-5eb73ffb491c",
   "metadata": {},
   "outputs": [],
   "source": [
    "dict1 = {\n",
    "    'city1': city,\n",
    "    'city2': town\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "e26461a7-d9e1-484c-9c40-e2ce44fe4402",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'city1': ['texus', 'clafornia', 'valicon city'],\n",
       " 'city2': ['vatican_city', 'texus', 'hollywood']}"
      ]
     },
     "execution_count": 113,
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
   "execution_count": 115,
   "id": "2454b2c3-a1bb-478a-8d42-efc3c6599a3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(dict1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "53d83b0e-1894-45f9-a522-c6b35913abd4",
   "metadata": {},
   "outputs": [],
   "source": [
    "car = pd.read_csv('time text2.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "f3c97c3c-5af8-4eaa-9b9c-44fd8f5ed7e1",
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
       "      <th>Index</th>\n",
       "      <th>Name</th>\n",
       "      <th>Id No</th>\n",
       "      <th>Week</th>\n",
       "      <th>Work</th>\n",
       "      <th>Present</th>\n",
       "      <th>Time</th>\n",
       "      <th>Basic</th>\n",
       "      <th>Salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>14</td>\n",
       "      <td>2024</td>\n",
       "      <td>4</td>\n",
       "      <td>58.0</td>\n",
       "      <td>5.00</td>\n",
       "      <td>2525</td>\n",
       "      <td>5566</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>52</td>\n",
       "      <td>21</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>52.0</td>\n",
       "      <td>2.00</td>\n",
       "      <td>24455</td>\n",
       "      <td>57555</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>24</td>\n",
       "      <td>28</td>\n",
       "      <td>2024</td>\n",
       "      <td>11</td>\n",
       "      <td>25.0</td>\n",
       "      <td>20.00</td>\n",
       "      <td>25525</td>\n",
       "      <td>3255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>5.0</td>\n",
       "      <td>23.00</td>\n",
       "      <td>25455</td>\n",
       "      <td>6633</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>44</td>\n",
       "      <td>12</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>25.0</td>\n",
       "      <td>2.00</td>\n",
       "      <td>25542</td>\n",
       "      <td>2525</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>56</td>\n",
       "      <td>25</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>35.0</td>\n",
       "      <td>2.00</td>\n",
       "      <td>20255</td>\n",
       "      <td>53365</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>4</td>\n",
       "      <td>52</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>24.0</td>\n",
       "      <td>22.00</td>\n",
       "      <td>525</td>\n",
       "      <td>23355</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "      <td>58</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0.02</td>\n",
       "      <td>2525</td>\n",
       "      <td>28556</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>9</td>\n",
       "      <td>522</td>\n",
       "      <td>85</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>32.0</td>\n",
       "      <td>55.00</td>\n",
       "      <td>5225</td>\n",
       "      <td>3652</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>10</td>\n",
       "      <td>23</td>\n",
       "      <td>87</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>22.0</td>\n",
       "      <td>22.00</td>\n",
       "      <td>225</td>\n",
       "      <td>6698</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>11</td>\n",
       "      <td>56</td>\n",
       "      <td>41</td>\n",
       "      <td>2024</td>\n",
       "      <td>41</td>\n",
       "      <td>55.0</td>\n",
       "      <td>25.00</td>\n",
       "      <td>2255</td>\n",
       "      <td>23255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>12</td>\n",
       "      <td>53</td>\n",
       "      <td>55</td>\n",
       "      <td>2024</td>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "      <td>25.00</td>\n",
       "      <td>255</td>\n",
       "      <td>32235</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>13</td>\n",
       "      <td>25</td>\n",
       "      <td>77</td>\n",
       "      <td>2024</td>\n",
       "      <td>5</td>\n",
       "      <td>0.3</td>\n",
       "      <td>25.00</td>\n",
       "      <td>252</td>\n",
       "      <td>23552</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>14</td>\n",
       "      <td>56</td>\n",
       "      <td>87</td>\n",
       "      <td>2024</td>\n",
       "      <td>6</td>\n",
       "      <td>0.0</td>\n",
       "      <td>25.00</td>\n",
       "      <td>223</td>\n",
       "      <td>23252</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>15</td>\n",
       "      <td>23</td>\n",
       "      <td>57</td>\n",
       "      <td>2024</td>\n",
       "      <td>9</td>\n",
       "      <td>23.0</td>\n",
       "      <td>65.00</td>\n",
       "      <td>2235</td>\n",
       "      <td>23225</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Index  Name  Id No  Week  Work  Present   Time   Basic   Salary\n",
       "0       1    47     14  2024     4     58.0    5.00   2525     5566\n",
       "1       2    52     21  2024     1     52.0    2.00  24455    57555\n",
       "2       3    24     28  2024    11     25.0   20.00  25525     3255\n",
       "3       4    41      1  2024     1      5.0   23.00  25455     6633\n",
       "4       5    44     12  2024     1     25.0    2.00  25542     2525\n",
       "5       6    56     25  2024     1     35.0    2.00  20255    53365\n",
       "6       7     4     52  2024     1     24.0   22.00    525    23355\n",
       "7       8     2     58  2024     1     26.0    0.02   2525    28556\n",
       "8       9   522     85  2024     1     32.0   55.00   5225     3652\n",
       "9      10    23     87  2024     1     22.0   22.00    225     6698\n",
       "10     11    56     41  2024    41     55.0   25.00   2255    23255\n",
       "11     12    53     55  2024     4     33.0   25.00    255    32235\n",
       "12     13    25     77  2024     5      0.3   25.00    252    23552\n",
       "13     14    56     87  2024     6      0.0   25.00    223    23252\n",
       "14     15    23     57  2024     9     23.0   65.00   2235    23225"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "72b6ce64-623b-474b-bca6-3a437455179d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(15, 9)"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "4dbe2e72-2f83-4167-a049-714b4d1208c2",
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
       "      <th>Index</th>\n",
       "      <th>Name</th>\n",
       "      <th>Id No</th>\n",
       "      <th>Week</th>\n",
       "      <th>Work</th>\n",
       "      <th>Present</th>\n",
       "      <th>Time</th>\n",
       "      <th>Basic</th>\n",
       "      <th>Salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>14</td>\n",
       "      <td>2024</td>\n",
       "      <td>4</td>\n",
       "      <td>58.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2525</td>\n",
       "      <td>5566</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>52</td>\n",
       "      <td>21</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>52.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>24455</td>\n",
       "      <td>57555</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>24</td>\n",
       "      <td>28</td>\n",
       "      <td>2024</td>\n",
       "      <td>11</td>\n",
       "      <td>25.0</td>\n",
       "      <td>20.0</td>\n",
       "      <td>25525</td>\n",
       "      <td>3255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>5.0</td>\n",
       "      <td>23.0</td>\n",
       "      <td>25455</td>\n",
       "      <td>6633</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>44</td>\n",
       "      <td>12</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>25.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>25542</td>\n",
       "      <td>2525</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Index  Name  Id No  Week  Work  Present   Time   Basic   Salary\n",
       "0      1    47     14  2024     4     58.0     5.0   2525     5566\n",
       "1      2    52     21  2024     1     52.0     2.0  24455    57555\n",
       "2      3    24     28  2024    11     25.0    20.0  25525     3255\n",
       "3      4    41      1  2024     1      5.0    23.0  25455     6633\n",
       "4      5    44     12  2024     1     25.0     2.0  25542     2525"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "9953164c-2810-4e1e-86a2-d02d41189cfa",
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
       "      <th>Index</th>\n",
       "      <th>Name</th>\n",
       "      <th>Id No</th>\n",
       "      <th>Week</th>\n",
       "      <th>Work</th>\n",
       "      <th>Present</th>\n",
       "      <th>Time</th>\n",
       "      <th>Basic</th>\n",
       "      <th>Salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>11</td>\n",
       "      <td>56</td>\n",
       "      <td>41</td>\n",
       "      <td>2024</td>\n",
       "      <td>41</td>\n",
       "      <td>55.0</td>\n",
       "      <td>25.0</td>\n",
       "      <td>2255</td>\n",
       "      <td>23255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>12</td>\n",
       "      <td>53</td>\n",
       "      <td>55</td>\n",
       "      <td>2024</td>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "      <td>25.0</td>\n",
       "      <td>255</td>\n",
       "      <td>32235</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>13</td>\n",
       "      <td>25</td>\n",
       "      <td>77</td>\n",
       "      <td>2024</td>\n",
       "      <td>5</td>\n",
       "      <td>0.3</td>\n",
       "      <td>25.0</td>\n",
       "      <td>252</td>\n",
       "      <td>23552</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>14</td>\n",
       "      <td>56</td>\n",
       "      <td>87</td>\n",
       "      <td>2024</td>\n",
       "      <td>6</td>\n",
       "      <td>0.0</td>\n",
       "      <td>25.0</td>\n",
       "      <td>223</td>\n",
       "      <td>23252</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>15</td>\n",
       "      <td>23</td>\n",
       "      <td>57</td>\n",
       "      <td>2024</td>\n",
       "      <td>9</td>\n",
       "      <td>23.0</td>\n",
       "      <td>65.0</td>\n",
       "      <td>2235</td>\n",
       "      <td>23225</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Index  Name  Id No  Week  Work  Present   Time   Basic   Salary\n",
       "10     11    56     41  2024    41     55.0    25.0   2255    23255\n",
       "11     12    53     55  2024     4     33.0    25.0    255    32235\n",
       "12     13    25     77  2024     5      0.3    25.0    252    23552\n",
       "13     14    56     87  2024     6      0.0    25.0    223    23252\n",
       "14     15    23     57  2024     9     23.0    65.0   2235    23225"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "28edfde5-6a80-4442-810e-0bad58abf793",
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
       "      <th>Index</th>\n",
       "      <th>Name</th>\n",
       "      <th>Id No</th>\n",
       "      <th>Week</th>\n",
       "      <th>Work</th>\n",
       "      <th>Present</th>\n",
       "      <th>Time</th>\n",
       "      <th>Basic</th>\n",
       "      <th>Salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>14</td>\n",
       "      <td>2024</td>\n",
       "      <td>4</td>\n",
       "      <td>58.0</td>\n",
       "      <td>5.00</td>\n",
       "      <td>2525</td>\n",
       "      <td>5566</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>52</td>\n",
       "      <td>21</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>52.0</td>\n",
       "      <td>2.00</td>\n",
       "      <td>24455</td>\n",
       "      <td>57555</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>24</td>\n",
       "      <td>28</td>\n",
       "      <td>2024</td>\n",
       "      <td>11</td>\n",
       "      <td>25.0</td>\n",
       "      <td>20.00</td>\n",
       "      <td>25525</td>\n",
       "      <td>3255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>5.0</td>\n",
       "      <td>23.00</td>\n",
       "      <td>25455</td>\n",
       "      <td>6633</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>44</td>\n",
       "      <td>12</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>25.0</td>\n",
       "      <td>2.00</td>\n",
       "      <td>25542</td>\n",
       "      <td>2525</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>56</td>\n",
       "      <td>25</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>35.0</td>\n",
       "      <td>2.00</td>\n",
       "      <td>20255</td>\n",
       "      <td>53365</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>4</td>\n",
       "      <td>52</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>24.0</td>\n",
       "      <td>22.00</td>\n",
       "      <td>525</td>\n",
       "      <td>23355</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "      <td>58</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0.02</td>\n",
       "      <td>2525</td>\n",
       "      <td>28556</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>9</td>\n",
       "      <td>522</td>\n",
       "      <td>85</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>32.0</td>\n",
       "      <td>55.00</td>\n",
       "      <td>5225</td>\n",
       "      <td>3652</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>10</td>\n",
       "      <td>23</td>\n",
       "      <td>87</td>\n",
       "      <td>2024</td>\n",
       "      <td>1</td>\n",
       "      <td>22.0</td>\n",
       "      <td>22.00</td>\n",
       "      <td>225</td>\n",
       "      <td>6698</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Index  Name  Id No  Week  Work  Present   Time   Basic   Salary\n",
       "0      1    47     14  2024     4     58.0    5.00   2525     5566\n",
       "1      2    52     21  2024     1     52.0    2.00  24455    57555\n",
       "2      3    24     28  2024    11     25.0   20.00  25525     3255\n",
       "3      4    41      1  2024     1      5.0   23.00  25455     6633\n",
       "4      5    44     12  2024     1     25.0    2.00  25542     2525\n",
       "5      6    56     25  2024     1     35.0    2.00  20255    53365\n",
       "6      7     4     52  2024     1     24.0   22.00    525    23355\n",
       "7      8     2     58  2024     1     26.0    0.02   2525    28556\n",
       "8      9   522     85  2024     1     32.0   55.00   5225     3652\n",
       "9     10    23     87  2024     1     22.0   22.00    225     6698"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "71dbc004-09bc-4a8d-a8b9-91f824cd7496",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(15, 9)"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "8063939f-d6fb-40d9-a36a-89969ddfd6b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1.0000e+00, 4.7000e+01, 1.4000e+01, 2.0240e+03, 4.0000e+00,\n",
       "        5.8000e+01, 5.0000e+00, 2.5250e+03, 5.5660e+03],\n",
       "       [2.0000e+00, 5.2000e+01, 2.1000e+01, 2.0240e+03, 1.0000e+00,\n",
       "        5.2000e+01, 2.0000e+00, 2.4455e+04, 5.7555e+04],\n",
       "       [3.0000e+00, 2.4000e+01, 2.8000e+01, 2.0240e+03, 1.1000e+01,\n",
       "        2.5000e+01, 2.0000e+01, 2.5525e+04, 3.2550e+03],\n",
       "       [4.0000e+00, 4.1000e+01, 1.0000e+00, 2.0240e+03, 1.0000e+00,\n",
       "        5.0000e+00, 2.3000e+01, 2.5455e+04, 6.6330e+03],\n",
       "       [5.0000e+00, 4.4000e+01, 1.2000e+01, 2.0240e+03, 1.0000e+00,\n",
       "        2.5000e+01, 2.0000e+00, 2.5542e+04, 2.5250e+03],\n",
       "       [6.0000e+00, 5.6000e+01, 2.5000e+01, 2.0240e+03, 1.0000e+00,\n",
       "        3.5000e+01, 2.0000e+00, 2.0255e+04, 5.3365e+04],\n",
       "       [7.0000e+00, 4.0000e+00, 5.2000e+01, 2.0240e+03, 1.0000e+00,\n",
       "        2.4000e+01, 2.2000e+01, 5.2500e+02, 2.3355e+04],\n",
       "       [8.0000e+00, 2.0000e+00, 5.8000e+01, 2.0240e+03, 1.0000e+00,\n",
       "        2.6000e+01, 2.0000e-02, 2.5250e+03, 2.8556e+04],\n",
       "       [9.0000e+00, 5.2200e+02, 8.5000e+01, 2.0240e+03, 1.0000e+00,\n",
       "        3.2000e+01, 5.5000e+01, 5.2250e+03, 3.6520e+03],\n",
       "       [1.0000e+01, 2.3000e+01, 8.7000e+01, 2.0240e+03, 1.0000e+00,\n",
       "        2.2000e+01, 2.2000e+01, 2.2500e+02, 6.6980e+03],\n",
       "       [1.1000e+01, 5.6000e+01, 4.1000e+01, 2.0240e+03, 4.1000e+01,\n",
       "        5.5000e+01, 2.5000e+01, 2.2550e+03, 2.3255e+04],\n",
       "       [1.2000e+01, 5.3000e+01, 5.5000e+01, 2.0240e+03, 4.0000e+00,\n",
       "        3.3000e+01, 2.5000e+01, 2.5500e+02, 3.2235e+04],\n",
       "       [1.3000e+01, 2.5000e+01, 7.7000e+01, 2.0240e+03, 5.0000e+00,\n",
       "        3.0000e-01, 2.5000e+01, 2.5200e+02, 2.3552e+04],\n",
       "       [1.4000e+01, 5.6000e+01, 8.7000e+01, 2.0240e+03, 6.0000e+00,\n",
       "        0.0000e+00, 2.5000e+01, 2.2300e+02, 2.3252e+04],\n",
       "       [1.5000e+01, 2.3000e+01, 5.7000e+01, 2.0240e+03, 9.0000e+00,\n",
       "        2.3000e+01, 6.5000e+01, 2.2350e+03, 2.3225e+04]])"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "44ebbc85-ee88-4319-9d35-3d3e513be0f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RangeIndex(start=0, stop=15, step=1)"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "car.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0df36da-9421-4939-82b6-c03cdac3b526",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
