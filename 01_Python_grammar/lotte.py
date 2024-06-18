{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62c6fa12-f17e-4759-b325-c2dbbc4239e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "def 로또_번호생성():\n",
    "    return random.sample(range(1, 46), 6)\n",
    "\n",
    "for i in range(5):\n",
    "    번호생성 = 로또_번호생성()\n",
    "    print(f\"Set {i + 1}: {번호생성}\")"
   ]
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
