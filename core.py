import time

for i in range(11):
    bar = "█" * i + "░" * (10 - i)
    print(bar, end="\r", flush=True)
    time.sleep(0.3)

print("\nDone!")

def inpt():
  an=str(input('What problem are you having?(headache, stomachache, cough, vomitting)'))
  if an == 'headache':
    print('Diagnosis:I understand, you have a brain no need to flex just use less')
  elif an == 'stomachache':
    print('Diagnosis:Eat less buddy, the foods are having civil war in your stomach')
  elif an == 'cough':
    print('Diagnosis:Wait?! I think you have breast cancer')
  elif an == 'vomitting':
    print('Diagnosis: If you are a boy then you are gay and if you are a girl then congrats mrs')
  else:
    print('No diagnosis bro cant you see I am skilled at those three diagnosis idiot')
inpt()
