all:
	gcc chall_1.c -Wall -o chall_1.bin -pie -fPIE
	gcc chall_2.c -Wall -o chall_2.bin -pie -fPIE
	gcc chall_3.c -Wall -o chall_3.bin -pie -fPIE
	gcc chall_4.c -Wall -o chall_4.bin
	gcc chall_5.c -Wall -o chall_5.bin -fno-stack-protector -z execstack -m32

fclean:
	rm -rf *.bin