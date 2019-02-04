section .data                           ;Data segment
   userMsg db 'Please enter a number: ' ;Ask the user to enter a number
   lenUserMsg equ $-userMsg             ;The length of the message
   plus db '+' 
   lenPlus equ $-plus
   
   newLine db '0x0a'
   lenNL equ $-newLine 
   
section .bss           ;Uninitialized data
   num resb 5
	
section .text          ;Code Segment
   global _start
	
_start:                ;User prompt
   mov eax, 4
   mov ebx, 1
   mov ecx, userMsg
   mov edx, lenUserMsg
   int 0x80

                ;Read and store the user input
   mov eax, 3
   mov ebx, 2
  
   mov ecx, num  ;your input is not an int, but a string. help. 

   mov edx, 5          ;5 bytes (numeric, 1 for sign) of that information
   int 0x80 

label:
   
   mov esi, 4 
   mov ebp, 35
   mov edi, 0 
   jmp stars 
   

   mov esi, 3 
   mov ebp, 42 
   mov edi, 0 
   jmp stars 
 
 ; Exit code
     
   mov eax, 1
   mov ebx, 0
   int 0x80
      

stars:   ;prints amount of stars in esi then returns to ebp line 

   mov eax, 4         ; system write 
   mov ebx, 1         ; exit code  

   mov ecx, plus      ; this is what we write  
   mov edx, lenPlus   ; this is how many bytes we write
   
   int 0x80     ;write it 
   
   inc edi 
   
   cmp edi, esi 
   jl stars ;  if edi is lower than esi, write another star 
   
   mov ecx, newLine 
   mov edx, lenNL  
   
   int 0x80 ;add a newline 
   
   jmp ebp ;jump back to origin 
   

   
   
   
   
   
   
   
   
   
   
   