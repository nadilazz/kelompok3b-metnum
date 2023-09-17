#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct daftar{
    char nama[25];
    char gender[10];
    int umur;
    struct daftar *next;
}Daf;

Daf * head;

Daf * createDaftar(char nama[25], char gender[10], int umur){
    Daf * New;
    New = (Daf*)malloc(sizeof(Daf));
    strcpy(New->nama,nama);
    strcpy(New->gender,gender);
    New->umur=umur;
    return New;
}

void input(char nama[25], char gender[10], int umur){
    Daf *add, *temp;
    add=createDaftar (nama, gender, umur);

    if(head==NULL || (add->umur > (head)->umur) || (add->umur == head->umur && strcmp(add->gender, "Perempuan")==0)){
        add->next=head;
        head=add;
    }else {
        Daf *temp=head;
        while (temp->next != NULL && (temp->next->umur > add->umur || (temp->next->umur == add->umur && strcmp(add->gender, "Laki-laki") == 0 && strcmp(temp->next->gender, "Laki-laki") == 0) ||(temp->next->umur == add->umur && strcmp(add->gender, "Laki-laki") == 0 && strcmp(temp->next->gender, "Perempuan") == 0) || (temp->next->umur == add->umur && strcmp(add->gender, "Perempuan") == 0 && strcmp(temp->next->gender, "Perempuan") == 0))){
            temp=temp->next;
        }
        add->next=temp->next;
        temp->next=add;
    }
}

void deleteAwal(){
    Daf *temp, *del;
    del = head;
    temp = head;
    head = temp->next;
    del->next = NULL;
    free(del);
    temp = NULL;
}

void printList(){
    if(head==NULL){
        printf("Daftar List Kosong\n");
    }else{
        Daf *temp = head;
        int i=1;
        while(temp != NULL){
            printf("%s\n", temp->nama);
            printf("%s\n", temp->gender);
            printf("%d\n", temp->umur);
            temp = temp->next;
            i++;
        }
    }
}

int main (){
    int instruksi, n, i, umur;
    char nama[25], gender[10];

    do{
        scanf("%d",&instruksi);
        switch(instruksi){
            case 0:
                exit(0);
                break;
            case 1:
                scanf("%d", &n);
                for(i=0; i<n; i++){
                    scanf(" %[^\n]", &nama);
                    scanf("%s", &gender);
                    scanf("%d", &umur);
                    input(nama, gender, umur);
                }
                break;
            case 2:
                scanf("%d", &n);
                for(i=0; i<n; i++){
                    if (head == NULL){
                    printf("\nDaftar List Kosong");
                    }else{
                        deleteAwal();    
                    }
                }
                break;
            case 3:
                printf("\n");
                printList();
                break;
        }
    }while(instruksi!=0);
	return 0;
}
