{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a196be2e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number: 20\n",
      "\n",
      "*\n",
      "**\n",
      "**\n",
      "**\n",
      "**\n",
      "**\n",
      "***\n",
      "***\n",
      "***\n",
      "***\n",
      "***\n",
      "***\n",
      "***\n",
      "***\n",
      "***\n",
      "***\n",
      "***\n",
      "***\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "x =int(input(\"enter a number: \"))\n",
    "\n",
    "for i in range(1,x):\n",
    "        if (i == 0):\n",
    "            print(\"*\"*i)\n",
    "        else:\n",
    "            print(math.ceil(math.log(i))*\"*\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a172600",
   "metadata": {},
   "source": [
    "# lab1\n",
    "**Thomas**\n",
    "\n",
    "1. sardines\n",
    "2. mayo\n",
    "3. ketchup\n",
    "\n",
    "![Planet9_3840x2160.jpg](attachment:Planet9_3840x2160.jpg)"
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
