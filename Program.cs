using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SPC_Crud
{
    class Customer
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int ProductId { get; set; }
        public int SupplierId { get; set; }
        public int Quantity { get; set; }
        public int Total { get; set; }
    }
    class Program
    {
        public static void ReadProducts()
        {
            SqlConnection con = new SqlConnection(); 
            con.ConnectionString = @"data source =IN5CG9214WT9\MSSQLSERVER01; database = newdb_dxc; integrated security = true";
            SqlCommand cmd = new SqlCommand(); 
            cmd.CommandText = "select * from Product";
            cmd.Connection = con;
            con.Open();
            SqlDataReader rdr = cmd.ExecuteReader();
            Console.WriteLine("PRODUCT\t\tPRODUCT ID");
            Console.WriteLine("-------\t\t----------");
            while (rdr.Read())
            {
                Console.WriteLine($"{rdr[1]}\t\t{rdr[0]}");
            }
            rdr.Close();
            con.Close();
        }

        public static void ReadSupplier(int index)
        {
            SqlConnection con = new SqlConnection(); 
            con.ConnectionString = @"data source =IN5CG9214Y4Y; database = SPC_CRUD; integrated security = true";
            SqlCommand cmd = new SqlCommand(); 
            cmd.CommandText = "select * from Supplier where ProductId = @index";
            cmd.Parameters.AddWithValue("index", index);
            cmd.Connection = con;
            con.Open();
            SqlDataReader rdr = cmd.ExecuteReader();
            Console.WriteLine("Product ID\t\tSupplierName\t\tSupplier ID\t\tLocation\t\tPrice");
            Console.WriteLine("------- --\t\t--------\t\t-------- --\t\t--------\t\t-----");
            while (rdr.Read())
            {
                Console.WriteLine($"{rdr["productid"]}\t\t{rdr["suppliername"]}\t\t{rdr["id"]}\t\t{rdr["location"]}\t\t{rdr["price"]}");
            }
            rdr.Close();
            con.Close();
        }

        public static int RetrievePrice(int productid, int supplierid)
        {
            int price = 0;
            SqlConnection con = new SqlConnection();
            con.ConnectionString = @"data source =IN5CG9214Y4Y; database = SPC_CRUD; integrated security = true";
            SqlCommand cmd = new SqlCommand(); 
            cmd.CommandText = "select Price from tblSupplier where ProdId = @p and Id=@s";
            cmd.Parameters.AddWithValue("p", productid);
            cmd.Parameters.AddWithValue("s", supplierid);
            cmd.Connection = con;
            con.Open();
            price = (int)cmd.ExecuteScalar();
            con.Close();
            return price;
        }

        public static string Retrieveproductname(int productid)
        {
            SqlConnection con = new SqlConnection();
            con.ConnectionString = @"data source =IN5CG9214Y4Y; database = SPC_CRUD; integrated security = true";
            SqlCommand cmd = new SqlCommand(); 
            cmd.CommandText = "select productname from Product where id = @p ";
            cmd.Parameters.AddWithValue("p", productid);
            cmd.Connection = con;
            con.Open();
            string name = (string)cmd.ExecuteScalar();
            con.Close();
            return name;
        }

        public static string Retrievesuppliername(int supplierid)
        {
            SqlConnection con = new SqlConnection();
            con.ConnectionString = @"data source =IN5CG9214Y4Y; database = SPC_CRUD; integrated security = true";
            SqlCommand cmd = new SqlCommand(); 
            cmd.CommandText = "select Name from Supplier where id = @s ";
            cmd.Parameters.AddWithValue("s", supplierid);
            cmd.Connection = con;
            con.Open();
            string suppliername = (string)cmd.ExecuteScalar();
            con.Close();
            return suppliername;
        }
        public static void InsertCustomer()
        {
            SqlConnection con = new SqlConnection(); 
            con.ConnectionString = @"data source =IN5CG9214Y4Y; database = SPC_CRUD; integrated security = true";
            SqlCommand cmd = new SqlCommand();
            Customer cust = new Customer();
            Console.WriteLine("Enter Customer ID : ");
            cust.Id = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter Customer name :");
            cust.Name = Console.ReadLine();
            Console.WriteLine("Select Product Id from list");
            ReadProducts();
            cust.ProductId = int.Parse(Console.ReadLine());
            Console.WriteLine("Select desired Supplier ID");
            ReadSupplier(cust.ProductId);
            cust.SupplierId = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter amount of product needed :");
            cust.Quantity = int.Parse(Console.ReadLine());
            int price = RetrievePrice(cust.ProductId, cust.SupplierId);
            cust.Total = cust.Quantity * price;
            cmd.CommandText = "insert into Customer values (@id,@customername,@productid,@supplierid,@totalamount)";
            cmd.Parameters.AddWithValue("id", cust.Id);
            cmd.Parameters.AddWithValue("customername", cust.Name);
            cmd.Parameters.AddWithValue("productid", cust.ProductId);
            cmd.Parameters.AddWithValue("supplierid", cust.SupplierId);
            cmd.Parameters.AddWithValue("totalamount", cust.Total);
            cmd.Connection = con;
            con.Open();
            int rowcount = cmd.ExecuteNonQuery();
            if (rowcount > 0)
            {
                Console.WriteLine("Record Inserted Successfully");
            }
            con.Close();
        }
        public static void DisplayBill()
        {
            SqlConnection con = new SqlConnection();
            con.ConnectionString = @"data source =IN5CG9214Y4Y; database = SPC_CRUD; integrated security = true";
            SqlCommand cmd = new SqlCommand();
            cmd.CommandText = "select * from Customer";
            cmd.Connection = con;
            con.Open();
            SqlDataReader rdr = cmd.ExecuteReader();
            while (rdr.Read())
            {
                Console.WriteLine($"{rdr[0]}\t\t{rdr[1]}\t\t{Retrieveproductname((int)rdr[2])}\t\t{Retrievesuppliername((int)rdr[3])}\t\t{rdr[4]}\t\t{rdr[5]}");
            }

            con.Close();
        }
        static void DisplayBill(int xId)
        {
            SqlConnection con = new SqlConnection();
            con.ConnectionString = @"data source =IN5CG9214Y4Y; database = SPC_CRUD; integrated security = true";
            SqlCommand cmd = new SqlCommand(); 
            cmd.CommandText = "select * from Customer where id = @id";
            cmd.Parameters.AddWithValue("id", xId);
            cmd.Connection = con;
            con.Open();
            SqlDataReader rdr = cmd.ExecuteReader();
            while (rdr.Read())
            {
                Console.WriteLine($"-----------BILL for {rdr["Name"]}----------");
                Console.WriteLine($"Product  : {Retrieveproductname((int)rdr[2])}");
                Console.WriteLine($"Sold By  : {Retrievesuppliername((int)rdr[3])}");
                Console.WriteLine($"Quantity : {rdr["Quantity"]}");
                Console.WriteLine($"Price    : {RetrievePrice((int)rdr[2], (int)rdr[3])}");
                Console.WriteLine($"Total    : {rdr[4]} X {RetrievePrice((int)rdr[2], (int)rdr[3])} = {rdr[5]}");
            }
            con.Close();
        }
        public static void Main(string[] args)
        {
            int y = 0;
            int choice;
            do
            {
                Console.WriteLine("1. New Customer Entry \n2. All Customer Details\n3.Customer Bill by ID");
                choice = int.Parse(Console.ReadLine());
                switch (choice)
                {
                    case 1:
                        InsertCustomer();
                        Console.ReadLine();
                        break;
                    case 2:
                        DisplayBill();
                        Console.ReadLine();
                        break;
                    case 3:
                        Console.WriteLine("Enter Customer Id to view bill");
                        int id = int.Parse(Console.ReadLine());
                        DisplayBill(id);
                        Console.ReadLine();
                        break;
                    default: Console.WriteLine("invalid"); break;
                }
                Console.WriteLine("Enter 1 to Continue 0 to exit");
                y = int.Parse(Console.ReadLine());
                if (y == 0)
                    Environment.Exit(1);
            } while (y == 1);
            Console.ReadLine();
        }
    }
}
