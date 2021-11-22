def myPow(self, x: float, n: int) -> float:
	if n == 0:
		return 1
	elif n == 1:
		return x
	elif n == -1:
		return 1 / x

	half_power = self.myPow(x, n // 2)
	power = half_power * half_power
	
	if n % 2 == 1:
		power *= x
	return power