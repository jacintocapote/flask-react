import Currency from "@/components/Dashboard/Currency";
import { Metadata } from "next";
import DefaultLayout from "@/components/Layouts/DefaultLaout";
import React from "react";
import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb";

export const metadata: Metadata = {
  title: "Currencies manage | Bank - Admin",
  description: "Page for manage currencies",
  // other metadata
};

const CurrencyPage: React.FC = () => {
  return (
    <DefaultLayout>
      <Breadcrumb pageName="Currencies" />
      <Currency/>

 
    </DefaultLayout>
  );
};

export default CurrencyPage;
