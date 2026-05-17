import matplotlib.pyplot as plt

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
new_births = [12, 15, 11, 9, 1, 9, 21]

plt.figure(1)
plt.plot(day, new_births, marker="o", linestyle=":", color="red")
plt.xlabel("Days")
plt.ylabel("New Births")

new_birth = [17, 5, 2, 11, 1, 8, 29]

plt.figure(2)
plt.plot(day, new_birth, marker="o", linestyle="--", color="green")
plt.xlabel("Days")
plt.ylabel("New Births")

plt.figure(3)
plt.plot(day, new_births, marker="o", linestyle=":", color="red", label="First")
plt.plot(day, new_birth, marker="o", linestyle="--", color="green", label="Second")
plt.xlabel("Days")
plt.ylabel("New Births")
plt.legend()

plt.show()

print("Attention!\nI wasn't able to visualize the data using mathematical problem...")