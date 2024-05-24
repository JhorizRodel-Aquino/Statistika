import ungroup
import group

print("\n[0]UNGROUPED DATA")
print("[1]GROUPED DATA")

while True:
    try:
        choice = input("\nEnter: ").upper()
    except:
        continue
    else:
        if choice == "0":
            ungroup.UNGROUPED()
        if choice == "1":
            group.GROUPED()
        if choice == "Q":
            break
