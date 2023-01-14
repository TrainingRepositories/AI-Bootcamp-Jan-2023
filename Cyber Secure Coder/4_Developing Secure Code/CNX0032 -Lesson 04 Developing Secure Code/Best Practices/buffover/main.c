#include <stdio.h>
#include <string.h>

int main(void) {
	
    char buff[15];
    int pass = 0;

    printf("\n Please enter the password > ");
    gets(buff);

    if (strcmp(buff, "password")) {
        printf (" Incorrect password. \n");
    } else {
        printf (" Correct password. \n");
        pass = 1;
    }

    if (pass) {
        printf (" You have been logged in with root privileges. \n");
    } else {
		printf (" Unable to log in. \n");
	}
	
	printf (" --------------------------------------------- \n");

    return 0;
}
