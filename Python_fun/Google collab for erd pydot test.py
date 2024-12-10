import pydot

# Membuat ERD menggunakan pydot
erd_graph = pydot.Dot(graph_type="digraph")

# Menambahkan entitas (tabel) ke dalam ERD
customer_node = pydot.Node("Pelanggan", shape="record", label="""\
{ Pelanggan | 
  { customer_id (PK) | name | address | phone }
}""")
product_node = pydot.Node("Produk", shape="record", label="""\
{ Produk | 
  { product_id (PK) | product_name | type | room_number | price_per_night }
}""")
transaction_node = pydot.Node("Transaksi", shape="record", label="""\
{ Transaksi | 
  { transaction_id (PK) | transaction_date | customer_id (FK) | check_in_date | check_out_date | duration }
}""")
transaction_detail_node = pydot.Node("Detail_Transaksi", shape="record", label="""\
{ Detail_Transaksi | 
  { detail_id (PK) | transaction_id (FK) | product_id (FK) | subtotal | total }
}""")
additional_fee_node = pydot.Node("Biaya_Tambahan", shape="record", label="""\
{ Biaya_Tambahan | 
  { fee_id (PK) | transaction_id (FK) | fee_type | amount }
}""")

# Menambahkan entitas ke dalam graph
erd_graph.add_node(customer_node)
erd_graph.add_node(product_node)
erd_graph.add_node(transaction_node)
erd_graph.add_node(transaction_detail_node)
erd_graph.add_node(additional_fee_node)

# Menambahkan relasi antar tabel
erd_graph.add_edge(pydot.Edge(customer_node, transaction_node, label="1", taillabel="N"))
erd_graph.add_edge(pydot.Edge(transaction_node, transaction_detail_node, label="1", taillabel="N"))
erd_graph.add_edge(pydot.Edge(product_node, transaction_detail_node, label="1", taillabel="N"))
erd_graph.add_edge(pydot.Edge(transaction_node, additional_fee_node, label="1", taillabel="N"))

# Menyimpan ERD sebagai file gambar PNG
erd_graph.write_png("ERD_Hotel_Transaction.png")

print("ERD berhasil dibuat dan disimpan sebagai ERD_Hotel_Transaction.png")
