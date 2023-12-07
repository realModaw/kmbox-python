#include "kmbox_interface.hpp"


// note : this is only for the kmbox b pro

inline void km_move(int X, int Y) {
	std::string command = "km.move(" + std::to_string(X) + "," + std::to_string(Y) + ")\r\n";
	send_command(hSerial, command.c_str());
}

inline void km_click() {
	std::string command = "km.left(" + std::to_string(1)  + ")\r\n"; // left mouse button down
	Sleep(10); // to stop it from crashing idk
	std::string command1 = "km.left(" + std::to_string(0) + ")\r\n"; // left mouse button up
	send_command(hSerial, command.c_str());
	send_command(hSerial, command1.c_str());
}

void main()
{
	int   X,
		  Y;
    string port = find_port("USB-SERIAL CH340"); // name of the kmbox port without ( COM )
	if (port.empty()) {
		std::cout << "\n	[!] no port found..";
		return;
	}


	if (!open_port(hSerial, port.c_str(), CBR_115200))  { // CBR_1115200 is the baud rate
		std::cout << "\n	[!] opening the port failed!";
		return;
	}

	std::cout << "\n	[+] connected to the kmbox with " + port;

	std::cout << "\n	[+] to which x cordinate do you wanna move?\n\n	-> ";
	std::cin >> X;

	std::cout << "\n	[+] to which y cordinate do you wanna move?\n\n	-> ";
	std::cin >> Y;

	km_move(X, Y);

	std::cout << "\n	[+] clicking left mouse button in 3 seconds\n";
	
	Sleep(3000);

	km_click();
	std::cout << "\n	[+] clicked your left mouse button!\n";
	_getch();

}
