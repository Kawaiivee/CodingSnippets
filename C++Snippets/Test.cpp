#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
	cout << "Hello World!" << endl;
	printf("HELLO WORLD\n");
	
	for(int i = 1; i < argc; i++){
		printf(argv[i]);
		printf("\n");
	}
	return 0;
}