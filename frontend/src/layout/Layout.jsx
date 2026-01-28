import { Outlet } from "react-router-dom";
import Nav from "../components/Nav";
import Footer from "../components/Footer";

const Layout = () => {
  return (
    <div className="min-h-screen flex flex-col bg-linear-to-br from-[#0b061a] via-[#2a0f45] to-[#3b0f6b]">

      <Nav />

      {/* CONTENIDO PRINCIPAL */}
      <main className="flex-1 flex overflow-hidden">
        <Outlet />
      </main>

      <Footer />
    </div>
  );
};

export default Layout;
