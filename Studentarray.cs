using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demo1
{
    class Studentarray
    {
        static void Main(string[] args)
        {
            int stud;
            Console.WriteLine("Enter Number of Students");
            stud = int.Parse(Console.ReadLine());
            String[] StuName = new String[stud];
            int[,] StuMarks = new int[stud, 5];
            int j = 0;
            int sum = 0;
            float avg = 0;
            for (int i = 0; i < stud; i++)
            {
                Console.WriteLine("Enter Student Name:");
                StuName[i] = Console.ReadLine();
                Console.WriteLine("Enter 5 Marks of Student");
                for (int k = 0; k < 5; k++)
                {
                    StuMarks[j, k] = int.Parse(Console.ReadLine());
                }
                j++;
            }
            Console.WriteLine();
            for (int i = 0; i < stud; i++)
            {
                sum = 0;
                Console.Write(StuName[i] + "\t");
                for (int k = 0; k < 5; k++)
                {
                    Console.Write(StuMarks[i, k] + "\t");
                    sum = sum + StuMarks[i, k];
                }
                avg = sum / 5;
                Console.Write(sum + "\t");
                Console.Write(avg + "\t");
                Console.WriteLine();
            }
            Console.ReadLine();
        }
    }
}