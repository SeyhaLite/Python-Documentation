"""បង្ហាញរបៀបទទួល argument ពីបន្ទាត់ពាក្យបញ្ជាតាម sys.argv។"""

import sys

print(sys.argv)

args = sys.argv[1:]
print("ចំនួន argument (មិនរាប់ឈ្មោះឯកសារ):", len(args))

if args:
    print("argument ដំបូង:", args[0])
