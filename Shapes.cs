using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CalculateVolume
{
    class Shapes
    {
        public float length, breadth, tri_base, height, radius, side;
        static void Main(string[] args)
        {
            Shapes a = new Shapes();
            a.Rectangle();
            a.Circle();
            a.Square();
            a.Triangle();
        }
        public void Rectangle()
        {
            Console.WriteLine("Enter the Length for Rectangle");
            length = float.Parse(Console.ReadLine());
            Console.WriteLine("Enter the breadth for Rectangle");
            breadth = float.Parse(Console.ReadLine());
            Console.WriteLine("Area of rectangle is :{0}", length * breadth);
            Console.ReadLine();
        }
        public void Circle()
        {
            Console.WriteLine("Enter the Radius of the Circle");
            radius = float.Parse(Console.ReadLine());
            Console.WriteLine("Area of Circle is:{0}", 3.14 * radius * radius);
            Console.ReadLine();
        }
        public void Square()
        {
            Console.WriteLine("Enter the side of a square");
            side = float.Parse(Console.ReadLine());
            Console.WriteLine("Area of Square is:{0}", side * side);
            Console.ReadLine();
        }
        public void Triangle()
        {
            Console.WriteLine("Enter the tri_base for Triangle ");
            tri_base = float.Parse(Console.ReadLine());
            Console.WriteLine("Enter the Height for Triangle ");
            height = float.Parse(Console.ReadLine());
            Console.WriteLine("Area of Triangle is:{0}", (tri_base * height) / 2);
            Console.ReadLine();
        }
        
    }
}
